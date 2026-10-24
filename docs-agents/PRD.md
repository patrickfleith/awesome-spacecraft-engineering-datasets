# Project context

## Purpose

Awesome Spacecraft Engineering Datasets helps industry practitioners and researchers find datasets related to space vehicle engineering and related fields. The public catalog lives in `README.md` and links to external dataset hosts.

## Audience and needs

- Researchers need datasets for experiments and machine learning benchmarks.
- Engineers need to compare datasets by task, size, format, and engineering context.
- Contributors need a consistent way to propose additions through GitHub issues.

## Existing content requirements

The README generator and dataset submission template establish the current entry format:

- Group entries by spacecraft subsystem or domain, with a cross-reference by task.
- Include the dataset name and source link.
- Describe the dataset, its intended task, size, and data format where available.
- Credit authors or provide a citation where available.
- Show tasks, label availability, and data origin as badges. Mark an unchecked licence as `unverified`.
- Identify announced datasets that are not yet available.

## Scope

The repository maintains a curated Markdown list. Dataset providers host the linked data. The repository contains no dataset processing pipeline or application code.

## Maintenance

Edit dataset entries and controlled vocabularies in `scripts/build-readme.py`, then run `python3 scripts/build-readme.py` from the repo root to regenerate `README.md`. The generator validates domain, task, and origin values and rejects missing tasks or empty licences. YAML dataset cards remain planned under DEC-001.

Check source material before changing factual metadata. Use `.github/ISSUE_TEMPLATE/dataset-submission.md` for proposed additions. A GitHub Actions workflow checks external catalog links weekly and on manual runs; it also runs the link checker tests. See `docs-agents/STACK.md` for validation commands. No formal success metrics or release process are documented.
