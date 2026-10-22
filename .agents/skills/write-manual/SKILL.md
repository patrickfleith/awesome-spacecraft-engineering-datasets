---
name: write-manual
description: Write or update docs-agents/SUM.md — the Software User Manual — from the codebase. Mode 1 (generate) builds a full, detailed SUM from scratch by inventorying every user-facing surface so nothing is missed. Mode 2 (update) revises the SUM against a PR/diff, removing what's obsolete, editing what changed, and adding what's new — precisely and concisely. Triggered by "write the manual", "generate the user manual", "document how to use this", or "update the manual for this PR".
---

# write-manual

Maintains `docs-agents/SUM.md` — the end-user manual: how to install and use the software correctly. Follows the template in `templates/docs-agents/SUM.md`: a **Contents** map up top, then 9 sections (§6–8 optional). This is a **user** manual, not a design doc — no internals, architecture, or rationale.

## The Contents block

A SUM is long, so `docs-agents/SUM.md` opens with a `## Contents` map — the first thing an agent or human reads to jump to the right passage. Build it from the actual headings (never guess), and **rebuild it after every change so it always matches the document** (see Mode 1 Step C and Mode 2 step 4).

- One entry per `##` section, and one **nested** sub-entry per `### Feature: <name>` subsection under §5, in document order.
- Each entry is a heading anchor link + ` — ` + a one-line "what's here". For a feature, the one-liner is what the feature does.
- Anchor = heading text lowercased, punctuation dropped, spaces → hyphens. E.g. `## 6. Configuration & Security` → `#6-configuration--security`; `### Feature: Export data` → `#feature-export-data`.
- List only sections/features that actually exist — omit entries for dropped optional sections (§6–8). Never list the Contents block itself.

## Before writing (both modes)

1. **Read the template** `templates/docs-agents/SUM.md` for the target structure.
2. **Read `docs-agents/GLOSSARY.md`** — use its canonical terms verbatim; never invent a synonym for something the glossary already names.
3. **Skim sibling docs for context, not for copying:** `docs-agents/PRD.md` (what & who it's for), `docs-agents/features/*` (feature intent), `README.md`, `docs-agents/CHANGELOG.md`. The SUM describes *how to use*, the PRD/FRD describe *what & why* — don't leak the latter in.

## Mode 1 — Generate a full SUM from the codebase

Goal: a complete manual with **no blind spots**. Blind spots come from documenting only the obvious entry point and missing the rest. Prevent that by **inventorying every user-facing surface first**, then writing.

**Step A — Inventory (do this before writing a word).** Sweep the codebase and list every surface a user touches:

| Surface | Where to look |
| --- | --- |
| Install / build | `package.json` scripts, `pyproject.toml`, `Dockerfile`, `Makefile`, install docs |
| Entry points | `bin/`, `main`, `cmd/`, `__main__`, CLI framework registrations |
| Commands / subcommands | arg-parser definitions (argparse/click/commander/cobra…) |
| API / endpoints | route definitions, OpenAPI/proto specs, exported public functions |
| Config & env vars | config schema, `.env.example`, settings files, defaults |
| Required files / services / credentials | DB, external APIs, secrets, tokens the software needs to run |
| Features | `docs-agents/features/*` and the code that implements them |
| Error/diagnostic messages | raised errors, exit codes, log strings a user would see |
| Prerequisites & platforms | supported OS/runtime, version constraints, dependencies |

Reconcile the inventory against the glossary and features docs. **Report the inventory to the user before drafting** if the surface is large — cheap way to catch a missing area early.

**Step B — Write.** Fill the template top to bottom. Map each inventory item to its section:
- Prereqs/platforms/required services → **§3 Requirements**
- Install + config + a verify-it-worked check → **§4 Installation**
- Every command/endpoint/feature → **§5 Usage** (one `### Feature: <name>` subsection each: what it does, how to use, example, options)
- Config keys, secrets/access, secure setup → **§6 Configuration & Security**
- Common errors → cause → fix, logs, recovery → **§7 Troubleshooting**
- Full command/config/env/error tables → **§8 Reference**

Every user-facing surface from Step A lands in exactly one section, or is deliberately dropped with a reason. Drop §6–8 only if genuinely empty.

**Step C — Build the Contents block.** Once the body is final, generate the `## Contents` map from the headings you actually wrote (per "The Contents block" above). This is the last step so the map matches the finished document.

## Mode 2 — Update the SUM for a PR

Goal: bring the SUM back in sync with reality **precisely and concisely** — touch only what the change touched. This is a surgical edit, not a rewrite.

1. **Get the diff.** `git diff <base>...HEAD` (or the PR range). Identify which user-facing surfaces changed — reuse the Step A inventory lenses, but scoped to the diff.
2. **Classify each SUM impact and act:**
   - **Remove** — a feature/command/flag/option the diff deleted → cut its lines (and its `### Feature:` subsection, reference row, error entry).
   - **Modify** — behavior, syntax, defaults, or steps changed → edit that passage in place; keep glossary terms.
   - **Add** — a new user-facing surface with no coverage → add the minimal section/`### Feature:` subsection/row needed.
3. **Leave untouched** anything the diff didn't affect. No reflowing, reordering, or "while I'm here" cleanups.
4. **Refresh the Contents block** — mandatory, not a "while I'm here" cleanup. If you added, removed, or renamed a section or `### Feature:` subsection, add/cut/rename its Contents entry; if a feature's purpose changed, update its one-liner. If no heading changed, leave Contents as-is.
5. **Report** a short changelist to the user: what you removed / modified / added and why (note any Contents change).

## Rules

- **User-facing only.** How to install, configure, and use it. No architecture, no design rationale, no code internals.
- **No blind spots (Mode 1):** inventory before drafting; every surface is covered or consciously dropped.
- **Surgical (Mode 2):** change only what the diff changed; don't rewrite stable sections.
- **Contents never goes stale.** After any edit, the `## Contents` map must match the document's headings exactly (right entries, right order, working anchors, one feature per `### Feature:` subsection). Regenerate it — this is required even in surgical Mode 2.
- **Glossary is law.** Use canonical terms; if the code reveals a user-facing concept the glossary is missing, flag it (suggest running `glossary`), don't coin a term silently.
- **Concise.** Fit the template; every example should be copy-pasteable. Cut prose that doesn't help a user act.
- **Verify examples exist.** Don't invent commands, flags, or endpoints — cite ones that are actually in the code.
- **Omit empty optional sections.** §6–8 carry `*(optional)*`; delete rather than pad.
