# Decisions

## TBD

No pending decisions recorded.

## Decided

### DEC-003 - Fix the dataset vocabulary and make every field state its own uncertainty

Decided by: Author with Agent
Date: 2026-10-24 00:00

**Decision:** Declare the controlled values in one block in `scripts/build-readme.py` and reject anything else at build time.

- `DOMAINS` is an explicit ordered list of `(domain, level, blurb)`. It is no longer derived from whichever entries happen to exist. Each domain carries a `level` from `LEVELS`: `system`, `subsystem`, `environment`, `adjacent`. Domain names follow the usual spacecraft product-tree names.
- A domain may be declared with no entries. It reserves the name and renders nothing until an entry lands. `Thermal control`, `Communications and TT&C`, and `Flight software` are declared empty today.
- `TASKS_VOCAB` and `ORIGIN_VOCAB` (`real`, `synthetic`, `mixed`) stay closed lists. `origin` supersedes the `real_or_synthetic` field named in DEC-001; it takes a list, because a dataset can be both.
- An unverified licence is the string `unverified`, not an empty field. Every entry carries a licence: a stated one, `no licence stated`, or `unverified`.
- `validate()` runs before any output and fails the build on an unknown domain, task, or origin, on an entry with no task, and on an empty licence.
- `config/dataset-vocabulary.yaml` is deleted. It held a draft vocabulary that was never enforced and that disagreed with the generator. Its scope rule and tagging rules are carried over as comments on the vocabulary block.

**Rationale:** Deriving the domain list from the entries meant deleting the last entry in a category silently deleted the category, and a typo silently created one. An explicit list that fails the build makes adding a category a deliberate edit. The `level` field separates a whole-mission concern from one subsystem box, which the flat list conflated: `GNC and space debris` mixed an onboard subsystem with the debris population and with two trajectory-optimisation challenges, and has been split into `GNC and AOCS`, `Space surveillance and debris`, and `Mission and trajectory design`.

Two vocabularies is worse than either one. The draft YAML was the richer list, with 22 defined tasks and 19 defined domains against the generator's 17 and 15, but it was marked draft, nothing read it, and adopting it meant reclassifying all 35 entries and taking a YAML dependency in a repo that has none. One enforced list in the file that already carries the entries is the cheaper correct answer; the richer distinctions can be added to it when an entry needs them.

An empty licence field renders as absence, which reads as "no licence" to someone scanning the page. `unverified` says the thing that is actually true: nobody has checked yet. Declaring empty domains answers the contributor question "where does this go" for a subsystem the catalogue has not reached.

### DEC-002 - Group the catalogue by subsystem or domain

Decided by: Author with Agent
Date: 2026-10-22 17:49

**Decision:** Group the README catalogue by spacecraft subsystem or domain (propulsion, power, structures, avionics, operations and telemetry, GNC, payload, space environment, text, astronomy) instead of by machine learning task. Keep a task cross-reference so task-driven readers can still find entries.

**Rationale:** A dataset often serves more than one task, so a task-first grouping forces an arbitrary choice or duplicate entries. Subsystem is a single stable property of the data and matches how engineers in the audience search.

### DEC-001 - Store concise dataset cards in YAML

Decided by: Author with Agent
Date: 2026-10-22 15:50

**Decision:** Store one YAML card per dataset under `datasets/` and generate the README from these cards, grouped by task. Require `name`, `url`, `task`, and `summary`, with summaries limited to two sentences; allow optional `domain`, `size`, `format`, `rows`, `labels`, `real_or_synthetic`, `licence`, `source`, `year`, `citation`, `added`, and `checked`, and omit unknown optional fields.

**Rationale:** A small required core supports datasets with sparse metadata, while structured fields support consistent descriptions, filtering, and export. Define the allowed task, domain, and other categorical values in a follow-up task.

**Revised (2026-10-22 17:49):** The README is grouped by subsystem or domain, not by task. See DEC-002. The YAML card format and its required fields are unchanged; `domain` becomes the grouping key and `task` stays a card field used for the cross-reference.

**Revised (2026-10-24):** `real_or_synthetic` is now `origin` and takes a list. An unverified licence is the string `unverified` rather than an omitted field, so the original rule that `licence=''` means not verified no longer holds. The allowed values for `domain`, `task`, and `origin` are fixed in DEC-003.
