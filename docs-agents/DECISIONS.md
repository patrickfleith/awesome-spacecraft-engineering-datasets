# Decisions

## TBD

No pending decisions recorded.

## Decided

### DEC-001 - Store concise dataset cards in YAML

Decided by: Author with Agent
Date: 2026-10-22 15:50

**Decision:** Store one YAML card per dataset under `datasets/` and generate the README from these cards, grouped by task. Require `name`, `url`, `task`, and `summary`, with summaries limited to two sentences; allow optional `domain`, `size`, `format`, `rows`, `labels`, `real_or_synthetic`, `licence`, `source`, `year`, `citation`, `added`, and `checked`, and omit unknown optional fields.

**Rationale:** A small required core supports datasets with sparse metadata, while structured fields support consistent descriptions, filtering, and export. Define the allowed task, domain, and other categorical values in a follow-up task.
