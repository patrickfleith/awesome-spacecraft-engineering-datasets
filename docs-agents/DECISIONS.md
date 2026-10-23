# Decisions

## TBD

No pending decisions recorded.

## Decided

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
