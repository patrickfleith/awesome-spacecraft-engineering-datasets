# Stack

- **Content:** Markdown dataset catalog in `README.md`.
- **Hosting and collaboration:** GitHub repository and issues.
- **Contribution intake:** Markdown issue template at `.github/ISSUE_TEMPLATE/dataset-request.md`.
- **Agent context:** agents-control docs, six repository skills, and generated Claude Code adapters.
- **Runtime and dependencies:** No application runtime, package manifest, or dependency manager. Link maintenance uses Python 3.13 and its standard library. Publishing reports uses the GitHub CLI included on GitHub-hosted Ubuntu runners.
- **Validation:** Review Markdown formatting, dataset metadata, citations, and source links. `.github/workflows/check-links.yml` tests the link checker on pull requests that change the checker or workflow. Scheduled and manual runs also check external links in `README.md`.

## Link maintenance

The **Check dataset links** workflow runs every Monday at 07:23 UTC and supports manual runs from GitHub Actions. It follows redirects, makes up to three attempts for temporary failures and rate limits, and honors `Retry-After` up to 60 seconds per retry. It checks all external catalog URLs, including supporting references, and deduplicates URLs across entries.

The workflow creates or updates one bot-owned issue, **Dataset links that need review**. It reopens that issue if findings return and closes it when all checks pass. Each run replaces the issue body, so keep investigation notes in comments. The run summary also contains the report. The workflow uses `GITHUB_TOKEN` with `contents: read` and `issues: write`; no separate secret is needed.

Reports list alerts only and omit working links and working redirects. Red alerts identify broken links. Yellow alerts identify unverified links and suspected soft 404s that need human review. Login requirements, bot blocks, exhausted rate limits, server failures, and network errors are unverified. Error titles or main headings, redirects to site homepages, and downloads redirected to HTML pages need human review. A clean run reports "No link alerts." The checker reads at most 256 KiB of HTML per response and does not execute JavaScript. Successful responses cannot prove that a dataset is still available.

Run a local check without GitHub credentials or issue updates:

```sh
python3 .github/scripts/check_links.py
```

Run the checker tests:

```sh
python3 -m unittest discover -s .github/scripts -p 'test_*.py' -v
```

Use `--report /path/to/report.md` to save a report. `--publish` also updates the issue and requires an authenticated `gh` CLI and `GH_REPO=owner/repo`. Link findings do not fail the workflow; execution errors and issue publication failures do.
