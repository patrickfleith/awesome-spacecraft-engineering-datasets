---
name: decide
description: Record decisions in docs-agents/DECISIONS.md — add a TBD (open question), log a decided decision, or revise/revoke an existing one. Use when the user says "decide", "we decided", "log a decision", "that's TBD", or wants to change/revoke a past decision
---

# decide

Maintains `docs-agents/DECISIONS.md`. Keep entries terse.

## Locate the file

Edit `docs-agents/DECISIONS.md` in the current project. If it doesn't exist, create it with this structure:

```markdown
# Decisions

## TBD

- **<Shortname> — <pending decision>** — options/context in one line.

## Decided

### DEC-001 — title

Decided by: Author | Author with Agent | Agent
Date: YYYY-MM-DD HH:MM

**Decision:** 1–2 sentences (what was decided).

**Rationale:** 1–2 sentences (why).
```

## Modes

**1. Add a TBD** (open question requiring a decision to move forward, not yet decided).
Not to be confused with an open question from `docs-agents/QUESTIONS.md` which do not related to decision.
Append to the `## TBD` list:
```
- **<Shortname> — <pending decision>** — options/context in one line.
```

**2. Log a decided decision**
- Find the highest `DEC-NNN` in `## Decided`; new id = highest + 1, zero-padded to 3 digits.
- Prepend the new entry to the top of `## Decided` (newest first).
- Get the timestamp by running `date "+%Y-%m-%d %H:%M"`.
- If it resolves a `## TBD` item, remove that TBD line.
```
### DEC-NNN — <title>

Decided by: Author | Author with Agent | Agent
Date: YYYY-MM-DD HH:MM

**Decision:** 1–2 sentences (what was decided).

**Rationale:** 1–2 sentences (why).
```
Set "Decided by" to who actually decided (ask if unclear; default `Author with Agent`).
`Author` means the person using the skill.
`Agent` means the coding agent harness in use.

**3. Revise a decision**
Locate the `DEC-NNN`. Do NOT rewrite history silently — append a revision note under the existing entry:
```
**Revised (YYYY-MM-DD HH:MM):** what changed and why. Supersedes original decision above.
```
Then move the whole entry to the top of `## Decided`. Keep its original id — the number is a stable reference, not a sort key, so recently-touched decisions surface first even if ids end up out of numeric order.

**4. Revoke a decision**
Prefix the title with `~~REVOKED~~` and append:
```
**Revoked (YYYY-MM-DD HH:MM):** reason. No longer in effect.
```
Then move the whole entry to the top of `## Decided` (same rule as revise) — a revocation is important activity, so surface the "no longer in effect" warning rather than leaving it buried.

## Rules

- Never renumber existing DEC ids.
- Always stamp real timestamps via `date`, never guess.
- Keep it skimmable — 1–2 sentences per field.
