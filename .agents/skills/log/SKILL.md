---
name: log
description: Quickly add one entry to the right doc — a task, idea, stack choice, concern, or open question — in the correct format. Triggered by "log"/"note"/"capture"/"add"/"jot down" + the kind, e.g. "log this task", "note this idea down", "capture a concern", "add TODO", "we're using X for Y — put it in the stack", "open question:". Addition only.
---

# log

Append a single new entry to the correct doc under `docs-agents/`, in that doc's format. This skill only **adds** — it never edits, reorders, or removes existing entries. Decisions and glossary terms are out of scope (use `decide` / `glossary`).

## Route by what the user is logging

Match on the **kind** the user names, however they phrase it (log / note / capture / add / jot down / write down / remember, or just naming the thing):

| Kind & example phrasings                                                       | File                       | What to do                            |
| ------------------------------------------------------------------------------ | -------------------------- | ------------------------------------- |
| **task** — "log this task", "add a TODO", "remind me to…", "we still need to…" | `docs-agents/TASKS.md`     | checkbox item at top of **To do**     |
| **idea** — "log this idea", "note this down", "what if we…", "idea:"           | `docs-agents/IDEAS.md`     | new `IDEA-NNN` at the top             |
| **stack** — "we're using X for Y", "put X in the stack", "we went with X"      | `docs-agents/STACK.md`     | add a `- **Category:** choice` bullet |
| **concern** — "log this concern", "I'm worried that…", "flag that…", "risk:"   | `docs-agents/CONCERNS.md`  | new `CON-NNN` at the top              |
| **question** — "log this question", "open question:", "we need to figure out…" | `docs-agents/QUESTIONS.md` | new `Q-NNN` at the top                |

**Newest goes on top.** Insert each new entry above the existing ones, not at the bottom. (Stack is the exception — it's grouped by category, not by recency.)

If the target file doesn't exist, create it with just its `# Heading` before adding the entry. For ID'd docs, next id = highest existing NNN + 1, zero-padded to 3.

## Formats

**Task** — `docs-agents/TASKS.md`, insert at the top of the `## To do` section:
```
- [ ] <task> <!-- optional (context) -->
```
The file is organized `## To do` / `## Done`. Create those sections if missing; leave completed items alone (they belong under `## Done`).

**Idea** — `docs-agents/IDEAS.md`, insert at top of the list (newest first):
```
## IDEA-NNN — <one-line title>

Brief note (10–50 words), or bullets.
```

**Stack** — `docs-agents/STACK.md`, add a bullet in its logical spot (grouped by category, parentheses only if extra detail helps):
```
- **<Category>:** <choice> (<detail>)
```
If that category already exists with a different value, don't overwrite — flag the conflict and ask.

**Concern** — `docs-agents/CONCERNS.md`, insert at top (newest first):
```
## CON-NNN — <one-line title>

What it is and why it matters (10–50 words). Ref: <url, if any>
```

**Question** — `docs-agents/QUESTIONS.md`, insert at top (newest first):
```
## Q-NNN — <the question> — `open`

**Answer:** <fill once answered; set status to `answered`>
```

## Rules

- **One entry per invocation**, inserted at the top — no rewriting the rest of the file.
- **Keep it tight.** Fit the format; don't pad. Rephrase the user's note only enough to be clear.
- **Never guess an id** — read the file, find the highest, increment.
- **Ambiguous target?** If it's unclear which doc the user means, ask before writing.
