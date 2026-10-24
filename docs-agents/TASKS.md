# Tasks

## To do

- [ ] Write short definitions for the `task` vocabulary and for the subsystem groups that carry no blurb. Deferred on 2026-10-24: the names are self-explanatory to the audience, so this earns little. The deleted `config/dataset-vocabulary.yaml` has usable drafts in git history if this is picked up. See DEC-003.
- [ ] Verify the licence for the 23 entries marked `unverified` against their host, and record the result. See DEC-003.
- [ ] Remove or rehome Statlog (Landsat Satellite). It sits in `Payload and instruments`, but land-cover classification is the named example of what the scope rule excludes. See DEC-003.

## Done

- [x] Fix the domain vocabulary as an explicit ordered list with a `level` per domain, rather than deriving it from whichever entries exist. Declare empty domains so a future entry has a home, and fail the build on an unknown value. See DEC-003.
- [x] State how a card handles an unverified categorical value. An unverified licence is the string `unverified`, never an empty field. See DEC-003.
- [x] Define the allowed `task` values. `TASKS_VOCAB` in `scripts/build-readme.py` fixes 17 values, and an entry carries every task it supports rather than one headline task.
- [x] Define the allowed origin values. `real`, `synthetic`, and `mixed`, carried as a list and rendered as badges. This replaces the `real_or_synthetic` field named in DEC-001.
- [x] Add a weekly GitHub Action to check dataset links and open or update an issue for broken links. Handle redirects, retry temporary failures and rate limits, and flag suspected soft 404s for review.
- [x] Set up agents-control with repository context, project skills, and Claude Code adapters.
