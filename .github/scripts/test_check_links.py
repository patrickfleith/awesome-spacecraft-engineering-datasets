from datetime import datetime, timezone
from email.utils import format_datetime
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import threading
import unittest
from unittest.mock import Mock, patch
from urllib.error import URLError

import check_links as checker


class Handler(BaseHTTPRequestHandler):
    counts = {}

    def do_GET(self):
        self.counts[self.path] = self.counts.get(self.path, 0) + 1
        status, headers, body = 200, {}, '<title>Dataset catalog</title>'
        if self.path in {'/redirect', '/dataset.pdf'}:
            status, headers = 302, {'Location': '/ok'}
        elif self.path == '/homepage':
            status, headers = 301, {'Location': '/'}
        elif self.path == '/loop':
            status, headers = 302, {'Location': '/loop'}
        elif self.path == '/missing':
            status = 404
        elif self.path == '/gone':
            status = 410
        elif self.path == '/login':
            status = 401
        elif self.path == '/blocked':
            status = 403
        elif self.path == '/rate-limit':
            status, headers = 429, {'Retry-After': '0'}
        elif self.path == '/temporary' and self.counts[self.path] < 3:
            status, headers = 503, {'Retry-After': '0'}
        elif self.path == '/soft-404':
            body = '<title>Dataset host</title><h1>Dataset has been deleted</h1>'
        elif self.path == '/normal-body':
            body += '<p>Missing values and not found labels are part of the dataset.</p>'
        elif self.path == '/download':
            headers['Content-Type'] = 'application/octet-stream'
            body = '<title>404</title>'
        self.send_response(status)
        self.send_header('Content-Type', headers.pop('Content-Type', 'text/html; charset=utf-8'))
        for key, value in headers.items():
            self.send_header(key, value)
        self.end_headers()
        self.wfile.write(body.encode())

    def log_message(self, *args):
        pass


class LinkTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = ThreadingHTTPServer(('127.0.0.1', 0), Handler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()
        cls.base = f'http://127.0.0.1:{cls.server.server_port}'

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join()

    def setUp(self):
        Handler.counts.clear()
        self.sleep = patch.object(checker.time, 'sleep').start()
        self.addCleanup(patch.stopall)

    def check(self, path):
        return checker.check_link((self.base + path, [4]))

    def test_extract_markdown_reference_bare_and_nested_urls(self):
        text = ('[**Dataset**](https://host.test/Statlog+(Landsat+Satellite))\n'
                '<https://host.test/page?a=1&amp;b=2>\n'
                '[ref]: https://host.test/data\n'
                'Raw https://host.test/data.\n'
                '[again](https://host.test/data#section)')
        self.assertEqual(checker.extract_links(text), {
            'https://host.test/Statlog+(Landsat+Satellite)': [1],
            'https://host.test/page?a=1&b=2': [2],
            'https://host.test/data': [3, 4, 5],
        })

    def test_redirect_is_followed(self):
        result = self.check('/redirect')
        self.assertEqual(result.kind, 'ok')
        self.assertEqual(result.final_url, self.base + '/ok')

    def test_redirect_loop_is_reported(self):
        self.assertEqual(self.check('/loop').kind, 'broken')

    def test_missing_and_gone_are_broken_without_retries(self):
        for path in ('/missing', '/gone'):
            self.assertEqual(self.check(path).kind, 'broken')
            self.assertEqual(Handler.counts[path], 1)

    def test_temporary_failure_recovers(self):
        self.assertEqual(self.check('/temporary').kind, 'ok')
        self.assertEqual(Handler.counts['/temporary'], 3)
        self.assertEqual(self.sleep.call_count, 2)

    def test_rate_limits_and_bot_blocks_are_unverified_after_retries(self):
        for path in ('/rate-limit', '/blocked'):
            self.assertEqual(self.check(path).kind, 'unverified')
            self.assertEqual(Handler.counts[path], checker.ATTEMPTS)

    def test_login_requirement_is_unverified(self):
        self.assertEqual(self.check('/login').kind, 'unverified')

    def test_network_failure_is_retried(self):
        with patch.object(checker, 'urlopen', side_effect=URLError('timeout')) as request:
            self.assertEqual(self.check('/ok').kind, 'unverified')
        self.assertEqual(request.call_count, checker.ATTEMPTS)

    def test_soft_404_and_homepage_redirect_need_review(self):
        for path in ('/soft-404', '/homepage', '/dataset.pdf'):
            self.assertEqual(self.check(path).kind, 'review')

    def test_error_text_in_body_and_binary_download_are_ok(self):
        for path in ('/normal-body', '/download'):
            self.assertEqual(self.check(path).kind, 'ok')

    def test_retry_after_seconds_dates_invalid_and_cap(self):
        self.assertEqual(checker.retry_delay('12', 0), 12)
        self.assertEqual(checker.retry_delay('9999', 0), 60)
        self.assertEqual(checker.retry_delay('invalid', 1), 4)
        with patch.object(checker.time, 'time', return_value=0):
            date = format_datetime(datetime.fromtimestamp(30, timezone.utc), usegmt=True)
            self.assertEqual(checker.retry_delay(date, 0), 30)

    def test_report_includes_source_lines_and_final_url(self):
        report = checker.make_report([self.check('/homepage'), self.check('/missing')])
        self.assertIn('🔴 Broken: 1. 🟡 Review needed: 1.', report)
        self.assertIn('## 🔴 Broken links', report)
        self.assertIn('## 🟡 Suspected soft 404s', report)
        self.assertIn('README.md lines 4', report)
        self.assertIn('Final URL:', report)

    def test_report_omits_working_links_and_redirects(self):
        report = checker.make_report([
            self.check('/ok'), self.check('/redirect'), self.check('/blocked'),
        ])
        self.assertIn('## 🟡 Unverified links', report)
        self.assertIn(self.base + '/blocked', report)
        self.assertNotIn(self.base + '/ok', report)
        self.assertNotIn(self.base + '/redirect', report)
        self.assertNotIn('Working redirects', report)
        self.assertNotIn('## 🔴 Broken links', report)

    def test_clean_report_has_no_alert_sections_or_working_links(self):
        report = checker.make_report([self.check('/ok'), self.check('/redirect')])
        self.assertIn('No link alerts.', report)
        self.assertNotIn(self.base, report)
        self.assertNotIn('🔴', report)
        self.assertNotIn('🟡', report)


class IssueTests(unittest.TestCase):
    def setUp(self):
        patch.dict(checker.os.environ, {'GH_REPO': 'owner/repo'}).start()
        self.addCleanup(patch.stopall)

    def issue(self, state='open', number=42):
        return {'number': number, 'state': state, 'body': checker.MARKER,
                'user': {'type': 'Bot'}}

    def test_first_failing_run_creates_issue(self):
        api = Mock(side_effect=[[], {}])
        checker.sync_issue('report', True, api)
        self.assertEqual(api.call_args.args, ('POST', 'repos/owner/repo/issues',
                         {'title': checker.TITLE, 'body': 'report'}))

    def test_existing_issue_is_updated_and_closed_issue_is_reopened(self):
        for state in ('open', 'closed'):
            api = Mock(side_effect=[[self.issue(state)], {}])
            checker.sync_issue('report', True, api)
            self.assertEqual(api.call_args.args, ('PATCH', 'repos/owner/repo/issues/42',
                             {'title': checker.TITLE, 'body': 'report', 'state': 'open'}))

    def test_clean_run_closes_open_issue(self):
        api = Mock(side_effect=[[self.issue()], {}])
        checker.sync_issue('clean report', False, api)
        self.assertEqual(api.call_args.args, ('PATCH', 'repos/owner/repo/issues/42',
                         {'body': 'clean report', 'state': 'closed', 'state_reason': 'completed'}))

    def test_clean_run_without_open_issue_does_not_write(self):
        for issues in ([], [self.issue('closed')]):
            api = Mock(return_value=issues)
            checker.sync_issue('report', False, api)
            self.assertEqual(api.call_count, 1)

    def test_issue_lookup_paginates_and_excludes_humans_and_pull_requests(self):
        human = self.issue(number=8)
        human['user'] = {'type': 'User'}
        pull_request = dict(self.issue(number=9), pull_request={})
        api = Mock(side_effect=[[human, pull_request] * 50, [self.issue()], {}])
        checker.sync_issue('report', True, api)
        self.assertIn('page=2', api.call_args_list[1].args[1])
        self.assertEqual(api.call_args.args[1], 'repos/owner/repo/issues/42')

    def test_open_issue_is_preferred_over_newer_closed_issue(self):
        api = Mock(side_effect=[[self.issue('closed', 43), self.issue()], {}])
        checker.sync_issue('report', True, api)
        self.assertEqual(api.call_args.args[1], 'repos/owner/repo/issues/42')


if __name__ == '__main__':
    unittest.main()
