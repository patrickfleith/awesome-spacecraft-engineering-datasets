"""Check external catalog links and maintain one GitHub issue. Standard library only."""

import argparse
from concurrent.futures import ThreadPoolExecutor
from dataclasses import dataclass
from datetime import datetime, timezone
from email.utils import parsedate_to_datetime
import html
from html.parser import HTMLParser
import http.client
import json
import os
from pathlib import Path
import re
import subprocess
import time
from urllib.error import HTTPError, URLError
from urllib.parse import urldefrag, urlsplit
from urllib.request import Request, urlopen


MARKER = '<!-- dataset-link-check -->'
TITLE = 'Dataset links that need review'
ATTEMPTS = 3
TIMEOUT = 20
BODY_LIMIT = 256 * 1024
RETRYABLE = {403, 408, 425, 429, 500, 502, 503, 504}
MISSING = re.compile(
    r'\b(?:404|410|not found|page (?:is )?(?:missing|unavailable)|'
    r'(?:page|dataset|record|resource) (?:does not|doesn\'t) exist|'
    r'(?:page|dataset|record|resource) (?:has been |was )?(?:removed|deleted))\b',
    re.IGNORECASE,
)


@dataclass
class Result:
    url: str
    lines: list[int]
    kind: str
    detail: str
    final_url: str


def extract_links(text):
    """Read inline, reference, and bare HTTP URLs, including balanced parentheses."""
    links = {}
    for number, line in enumerate(text.splitlines(), 1):
        for match in re.finditer(r'https?://[^\s<>"\[\]]+', line):
            url = html.unescape(match.group()).rstrip('.,;:!*`')
            while url.endswith(')') and url.count(')') > url.count('('):
                url = url[:-1]
            url = urldefrag(url)[0]
            lines = links.setdefault(url, [])
            if number not in lines:
                lines.append(number)
    return links


class Headings(HTMLParser):
    def __init__(self):
        super().__init__()
        self.active = None
        self.parts = []
        self.headings = []

    def handle_starttag(self, tag, attrs):
        if tag in {'title', 'h1'}:
            self.active = tag
            self.parts = []

    def handle_data(self, data):
        if self.active:
            self.parts.append(data)

    def handle_endtag(self, tag):
        if tag == self.active:
            self.headings.append(' '.join(''.join(self.parts).split()))
            self.active = None


def soft_404_reason(original, final, body, is_html=True):
    headings = Headings()
    headings.feed(body)
    for heading in headings.headings:
        if MISSING.search(heading):
            return f'HTTP success with error heading: {heading[:160]}'
    source, target = urlsplit(original), urlsplit(final)
    if (original != final and is_html
            and re.search(r'\.(?:pdf|zip|gz|tar|csv|mat|npy|parquet)$', source.path, re.IGNORECASE)):
        return 'Download URL redirected to an HTML page'
    if source.path.strip('/') and not target.path.strip('/') and not target.query:
        return 'Redirected from a specific page to a site homepage'
    return None


def retry_delay(value, attempt):
    """Honor Retry-After seconds or HTTP dates, capped at 60 seconds per retry."""
    try:
        seconds = float(value)
    except (TypeError, ValueError):
        try:
            seconds = parsedate_to_datetime(value).timestamp() - time.time()
        except (TypeError, ValueError, OverflowError):
            seconds = 2 ** (attempt + 1)
    return max(0, min(seconds, 60))


def check_link(item):
    url, lines = item
    for attempt in range(ATTEMPTS):
        delay = None
        try:
            request = Request(url, headers={
                'User-Agent': 'SpacecraftDatasetLinkChecker/1.0',
                'Accept': 'text/html,application/xhtml+xml,*/*;q=0.8',
            })
            # GET catches error pages returned with HTTP 200. Bound reads for downloads.
            with urlopen(request, timeout=TIMEOUT) as response:
                final = response.url
                content_type = response.headers.get_content_type()
                reason = None
                if content_type in {'text/html', 'application/xhtml+xml'}:
                    body = response.read(BODY_LIMIT).decode(
                        response.headers.get_content_charset() or 'utf-8', errors='replace'
                    )
                    reason = soft_404_reason(url, final, body)
                else:
                    reason = soft_404_reason(url, final, '', is_html=False)
                return Result(url, lines, 'review' if reason else 'ok',
                              reason or f'HTTP {response.status}', final)
        except HTTPError as error:
            status, final = error.code, error.url
            delay = retry_delay(error.headers.get('Retry-After'), attempt)
            error.close()
            kind = 'unverified' if status in {401, 403, 408, 425, 429} or status >= 500 else 'broken'
            result = Result(url, lines, kind, f'HTTP {status}', final)
            if status not in RETRYABLE:
                return result
        except (URLError, OSError, http.client.HTTPException, ValueError, LookupError) as error:
            result = Result(url, lines, 'unverified', str(error)[:200], url)
        if attempt + 1 < ATTEMPTS:
            time.sleep(delay if delay is not None else retry_delay(None, attempt))
    result.detail += f' after {ATTEMPTS} attempts'
    return result


def make_report(results):
    counts = {kind: sum(r.kind == kind for r in results)
              for kind in ('broken', 'unverified', 'review')}
    warnings = counts['unverified'] + counts['review']
    report = [MARKER, '# Dataset link check', '',
              f'Checked {len(results)} unique external URLs in README.md at '
              f'{datetime.now(timezone.utc).isoformat(timespec="seconds")}.', '']
    if counts['broken'] or warnings:
        report.extend([f'🔴 Broken: {counts["broken"]}. 🟡 Review needed: {warnings}.', '',
                       'Yellow alerts need human review. They may reflect login requirements, '
                       'bot blocks, temporary failures, or suspected soft 404s.', '',
                       'This issue body is replaced on each run. Keep investigation notes in comments.', ''])
    else:
        report.extend(['No link alerts.', ''])
    for kind, title in [('broken', '🔴 Broken links'), ('unverified', '🟡 Unverified links'),
                        ('review', '🟡 Suspected soft 404s')]:
        items = [r for r in results if r.kind == kind]
        if not items:
            continue
        report.extend([f'## {title}', ''])
        for result in items:
            lines = ', '.join(map(str, result.lines))
            # Keep remote headings on one line in the report.
            detail = html.escape(' '.join(result.detail.split()), quote=True)
            report.extend([f'- {html.escape(result.url, quote=True)}',
                           f'  - README.md lines {lines}. {detail}'])
            if result.final_url != result.url:
                report.append(f'  - Final URL: {html.escape(result.final_url, quote=True)}')
        report.append('')
    server = os.environ.get('GITHUB_SERVER_URL', 'https://github.com')
    repo, run = os.environ.get('GITHUB_REPOSITORY'), os.environ.get('GITHUB_RUN_ID')
    if repo and run:
        report.append(f'[Workflow run]({server}/{repo}/actions/runs/{run})')
    return '\n'.join(report) + '\n'


def github_api(method, path, data=None):
    command = ['gh', 'api', '--method', method, path]
    if data is not None:
        command += ['--input', '-']
    response = subprocess.run(command, input=json.dumps(data) if data is not None else None,
                              text=True, capture_output=True, check=True)
    return json.loads(response.stdout)


def sync_issue(report, has_findings, api=github_api):
    repo = os.environ['GH_REPO']
    endpoint = f'repos/{repo}/issues'
    matches = []
    page = 1
    while True:
        issues = api('GET', f'{endpoint}?state=all&sort=created&direction=desc&per_page=100&page={page}')
        matches.extend(issue for issue in issues
                       if 'pull_request' not in issue
                       and issue.get('user', {}).get('type') == 'Bot'
                       and MARKER in (issue.get('body') or ''))
        if len(issues) < 100:
            break
        page += 1
    issue = next((issue for issue in matches if issue['state'] == 'open'),
                 matches[0] if matches else None)
    if has_findings:
        data = {'title': TITLE, 'body': report, 'state': 'open'}
        if issue:
            api('PATCH', f'{endpoint}/{issue["number"]}', data)
        else:
            api('POST', endpoint, {'title': TITLE, 'body': report})
    elif issue and issue['state'] == 'open':
        api('PATCH', f'{endpoint}/{issue["number"]}',
            {'body': report, 'state': 'closed', 'state_reason': 'completed'})


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--readme', type=Path, default=Path('README.md'))
    parser.add_argument('--report', type=Path)
    parser.add_argument('--publish', action='store_true', help='Update the GitHub issue using gh')
    args = parser.parse_args()
    links = extract_links(args.readme.read_text(encoding='utf-8'))
    if not links:
        parser.error('No external links found; refusing to publish an empty check')
    with ThreadPoolExecutor(max_workers=4) as executor:
        results = list(executor.map(check_link, links.items()))
    report = make_report(results)
    print(report)
    if args.report:
        args.report.write_text(report, encoding='utf-8')
    if args.publish:
        sync_issue(report, any(result.kind != 'ok' for result in results))
    # Findings belong in the maintenance issue. Execution and API failures fail CI.


if __name__ == '__main__':
    main()
