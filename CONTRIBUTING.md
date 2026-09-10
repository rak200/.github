# Contributing

Every rak200 repository follows one end-to-end development cycle. It is written out, step by
step with the commands to run, in **`LIFECYCLE.md`** — carried into each repository by the
`.rak200/` submodule, and readable at its source:

**→ [rak200/workflow `LIFECYCLE.md`](https://github.com/rak200/workflow/blob/master/LIFECYCLE.md)**

That document is the entry point for a person *and* for an agent, and it covers the cycle: issue →
branch → work → PR → CI → review → merge → release → propagation. Two companions travel in the same
submodule and are named where you need them —
[**`CONTINGENCIES.md`**](https://github.com/rak200/workflow/blob/master/CONTINGENCIES.md) for when a
step goes wrong (a red gate, a check that never appears, a leaked credential, a stale pin, a bad
release), and
[**`REPOSITORY.md`**](https://github.com/rak200/workflow/blob/master/REPOSITORY.md) for onboarding a
repository and retiring one.

**One caveat worth stating rather than discovering.** This file propagates account-wide and
therefore always shows the **current** version. The copy in a repository's `.rak200/` is the
version **that repository pinned**. Both are correct for their reader; the pinned one governs
work done in the repo, and a divergence is closed by bumping the submodule.

## The short version

- Work happens on a short-lived branch off `master`; direct pushes are refused by the platform.
- The **PR title is the commit** — squash-only merges, and the title must be a
  [Conventional Commit](https://www.conventionalcommits.org). It drives the release.
- One check is required: **`ci / gate`**. Green merges; red does not.
- Releases are derived from commit history by `release-please`. Do not hand-edit versions.
