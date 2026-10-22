---
name: commit
description: Turn uncommitted work into a logically ordered sequence of atomic conventional commits. Surveys the whole working tree, groups changes, orders them foundation-first, shows a plan, then commits by path. Use when the user says "commit this", "commit my work", "split this into commits", or "clean up my changes into commits"
---

# commit

Take the current uncommitted work and commit it as a clean, ordered sequence of atomic commits — each self-consistent, each a conventional-commit.

## 1. Survey

Run these to see everything (not just what's staged):

```bash
git status --short
git diff            # unstaged
git diff --staged   # staged
```

Read the actual changes. List untracked files too (`git status --short` shows them as `??`).

If the user named a subset to commit (specific files, or "just the auth work"), scope everything below to that subset and leave the rest untouched. Otherwise consider the whole tree.

## 2. Group into atomic commits

Cluster the changes into the smallest units that each stand on their own (one logical change per commit). Split unrelated work apart; keep a change and its direct test/doc together.

**Flag unfinished work.** While reading the diff, watch for changes that look incomplete or not meant to ship — e.g. `TODO`/`FIXME`/`XXX` added, commented-out or debug code (`print`, `console.log`, `dbg!`), stubs / empty function bodies / `pass` / `NotImplementedError`, half-edited files, failing or `.skip`ped tests, or a reference with no definition. List each one and **ask** whether to include it, hold it back (leave unstaged), or fix it first. Don't silently commit it.

## 3. Order foundation-first

Sequence commits so each builds on the last:

1. Dependencies / config / build setup
2. Shared utilities, types, refactors that others depend on
3. Features / fixes that use them
4. Tests
5. Docs

## 4. Show the plan, wait for approval

Print the proposed sequence and stop:

```
1. feat(auth): add password reset endpoint
   files: src/auth/reset.ts, src/routes.ts
2. test(auth): cover password reset flow
   files: test/auth/reset.test.ts
```

Do not create any commit until the user approves. Adjust on feedback.

## 5. Commit sequentially

For each commit, stage that group **by path** then commit:

```bash
git add <paths for this commit>
git commit -m "<type>(<scope>): <description>" -m "- detail" -m "- detail"
```

- Stage by explicit paths only. Do **not** use `git add -p`/`git add -i` (interactive, unsupported here); if two logically separate changes live in the same file and can't be split by path, note it in the plan and commit them together.
- After each commit, verify with `git status` that the right files landed.

## Commit format

```
<type>(<scope>): <description>
```
Add a bullet body (`-m` per bullet) only when the change has multiple parts.

Types: `feat` (new feature), `fix` (bug fix), `refactor`, `perf`, `test`, `docs`, `build`, `ci`, `chore`. Scope is optional, lowercase, the affected area. Description: imperative, lowercase, no trailing period.

## Rules

- **Plan before committing.** Never commit without showing the sequence first.
- **Subset is fine.** Commit only the changes the user asked for; leave everything else exactly as it was.
- **Never commit unfinished work silently.** If something looks incomplete, ask first.
- **Clean messages.** No agent attribution footer — write them as a human would.
- **Never push.** Only `git push` if the user explicitly asks.
- **Don't commit junk.** If a file looks like a secret, credential, or large build artifact, leave it unstaged and flag it.
- **Branch safety.** If on the default branch (`main`/`master`), say so and offer to create a branch before committing.
- **Respect hooks.** If a pre-commit hook rejects or rewrites a commit, stop and report — don't loop or bypass with `--no-verify` unless asked.
