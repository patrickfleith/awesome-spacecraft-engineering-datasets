# AGENTS.md

Instructions for AI coding agents working in this repo. Codex and Cursor read
this file directly, Codex cloud tasks included. Claude Code reads it through the
one-line `CLAUDE.md` adapter (`@AGENTS.md`). Keep it compact and current.

## How to work here

- **What this is:** A curated list of spacecraft engineering and related space datasets for researchers and industry practitioners.
- Before acting, consult the relevant project doc below.
- Keep changes minimal and follow the existing Markdown entry format.
- Dataset entries belong in `README.md`; use `.github/ISSUE_TEMPLATE/dataset-request.md` for the expected metadata.
- Verify dataset facts against the linked source before adding or changing them.
- This repository has no application code, build system, or automated test suite.

## Writing rules

Everything you write follows `.agents/skills/unslop/SKILL.md`: answers in chat,
docs, commit messages, PR text. Read it before you write.

## Project docs

Project docs live in `docs-agents/`. Consult the relevant one before acting. If a
doc does not exist yet, do not fabricate one. Create it with the skill noted below.

| Doc | Path | What it captures | Skill |
|-----|------|------------------|-------|
| Dataset catalog | README.md | Public dataset list, categories, descriptions, and source links. | none |
| Dataset request | .github/ISSUE_TEMPLATE/dataset-request.md | Metadata requested for proposed additions. | none |
| Product context | docs-agents/PRD.md | Purpose, audience, and catalog content requirements. | none |
| Stack | docs-agents/STACK.md | Repository format, tools, and validation. | `log` |
| Roadmap | docs-agents/ROADMAP.md | Recorded future work. | none |
| Decisions | docs-agents/DECISIONS.md | Pending and settled decisions. | `decide` |
| Tasks | docs-agents/TASKS.md | Repo-level tasks. | `log` |
| Changelog | docs-agents/CHANGELOG.md | Notable repository changes. | none |

## Capabilities

Skills live in `.agents/skills/`, committed with the repository so local and
cloud sessions use the same workflows. Codex and Cursor discover that directory
natively; `.claude/skills/` is a **generated** adapter for Claude Code, which
reads only its own path.

Never edit `.claude/skills/` by hand. Write the skill in `.agents/skills/` and
run `agents-control adapters`. Invoke a skill as `/name` in Claude Code, `$name`
in Codex, or by asking for it in Cursor. Currently available:

- `commit`: turn uncommitted work into atomic conventional commits.
- `log`: append an entry to STACK, TASKS, IDEAS, CONCERNS, or QUESTIONS.
- `decide`: record and manage decisions in DECISIONS.
- `glossary`: add and refine agreed terms in GLOSSARY.
- `write-manual`: write or update the SUM from the codebase.
- `unslop`: writing rules for anything an agent writes. Always applies.
