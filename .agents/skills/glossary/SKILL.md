---
name: glossary
description: Manage docs-agents/GLOSSARY.md — add or refine a canonical term, extract terms from the current conversation, or audit for conflicts and duplicates. Use when the user says "define this term", "add to the glossary", "build a glossary", "what do we call this", or wants to harden terminology
---

# glossary

Maintains `docs-agents/GLOSSARY.md` — the single source of truth for what terms mean in this project. Reference doc: opinionated, tight, skimmable. No implementation details or code.

## Locate the file

Edit `docs-agents/GLOSSARY.md`. If it doesn't exist, create it with this structure:

```markdown
# Glossary

**<Term>** — one or two sentence definition in this project's context. _avoid:_ <synonyms to not use>
```

Format per term: a bold term, an em-dash, one or two sentences saying what it **is** (not what it does), and an optional `_avoid:_` list of synonyms to kill. One term per line. Keep alphabetical, or group under `##` subheadings only when natural clusters clearly emerge.

## Modes

**1. Add a term**
Append (or insert alphabetically) one line in the format above. Pick the best word as canonical; list rejected synonyms under `_avoid:_`.

**2. Refine a term**
Locate the existing line and tighten its definition or update its `_avoid:_` list in place. Don't duplicate the term.

**3. Extract from this conversation**
Scan the discussion for project/domain-specific nouns and concepts. For each: pick a canonical term, write a one or two sentence definition, and note synonyms actually used in the conversation under `_avoid:_`. Add all new terms; refine any already present.

**4. Audit**
Read the whole file and report (inline, to the user): duplicate/near-duplicate terms, definitions longer than two sentences, generic programming terms that don't belong, and any term used two ways. Propose fixes; apply on confirmation.

## Rules

- **Be opinionated.** One canonical term per concept; everything else goes under `_avoid:_`.
- **One or two sentences, define what it IS.** Cut anything longer.
- **Project-specific only.** Skip generic programming concepts (array, endpoint, timeout) unless they carry special meaning here.
- **Flag conflicts, don't silently overwrite.** If a new term clashes with an existing definition, surface it to the user and let them resolve it.
- **No implementation details.** This is a glossary, not a spec or scratchpad.
