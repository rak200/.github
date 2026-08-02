# CLAUDE.md

Guidance for Claude Code when working in this repository.

## What this repository is

`rak200/.github` holds the **GitHub-native** half of the ecosystem baseline: reusable CI
workflows, the canonical ruleset JSON, and the community health files GitHub propagates on its
own. It deliberately holds nothing else — the conventions, `LIFECYCLE.md`, the scaffold and the
onboarding script live in `rak200/workflow`.

## Rules that are not negotiable here

1. **Third-party actions are pinned by full commit SHA**, with the version in a trailing comment.
   A tag is a moving target; Dependabot keeps the pins alive.
2. **The aggregator's two lines stay as they are** — `if: always()` and equality with `success`.
   Each was earned by a measured failure in which the gate reported green and enforced nothing.
3. **A workflow that produces a required check carries no `paths:` filter.** A filtered run
   produces *no check at all*, and a PR that needs it waits forever — a deadlock, not a failure.
4. **`pull_request_target` is banned**, and untrusted values (PR titles, branch names, issue
   bodies) reach a script through `env:`, never through `${{ }}` interpolation in `run:`.
5. **A settings write is verified by reading it back**, never by its response code.
6. **Changing a scanner step's shape means keeping three ordered steps**: scan (capturing the
   exit code), upload the SARIF, then *enforce* the captured code in a separate step. Collapsing
   them is how a scanner silently stops blocking.

## Testing a change to the pipeline

This repository's own caller resolves the workflows with `./`, which pins them to the PR's
commit — so a change to `base.yml` is exercised by the PR that makes it. That covers the shape,
not the languages: a change to `php.yml` is only genuinely tested by a PR in a PHP repository
pointing at the branch.

**A gate that has never failed has never been tested.** After changing one, make it fail on
purpose once and confirm it blocks.
