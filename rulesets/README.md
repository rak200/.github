# Rulesets

The canonical protection for every rak200 repository, committed so it is versioned and
reproducible rather than clicked. Applied per repo — `rak200` is a personal account, and
organization rulesets need an organization.

```bash
gh api -X POST repos/rak200/<repo>/rulesets --input rulesets/branch-review.json
gh api -X POST repos/rak200/<repo>/rulesets --input rulesets/branch-checks.json
gh api -X POST repos/rak200/<repo>/rulesets --input rulesets/tag.json
gh api repos/rak200/<repo>/rulesets --jq '[.[] | {name,target,enforcement}]'   # read it back
```

## Why the branch protection is two rulesets and not one

It was one, `branch.json`, holding the review rule and the status-check rule together. It
is two because **a bypass is granted per ruleset, never per rule** — anything exempted from
the review requirement was exempted from `ci / gate` in the same stroke, which is the one
thing nothing may be exempted from.

Splitting it buys exactly one thing, and it is the thing `automerge.yml` needs:
`github-actions` bypasses `default-branch-review` and is a stranger to
`default-branch-checks`. The baseline bump merges without a review; it does not merge
without a green pipeline, and the platform — not a workflow — is what enforces that.

`dependabot` is deliberately **not** a bypass actor here. It looks like it should be, and
it does nothing: bypasses are consulted when an actor performs a merge, and Dependabot
never merges anything. Measured on `rak200/utils#8` — see the header of `automerge.yml`.

Three fields are load-bearing and each was earned by a measurement:

- **`bypass_actors` must be declared.** A repository admin is *not* implicitly exempt; without
  this entry even `--admin` cannot merge the Release PR, whose required check is absent by
  construction. That is why the admin entry appears on **both** branch rulesets: the absent
  check is a `default-branch-checks` problem, the missing review a `default-branch-review` one,
  and a Release PR trips both.
- **A bypass does not make a pull request mergeable.** It lets an actor merge one that is not.
  GitHub computes mergeability without consulting `bypass_actors` at all — a bypassed pull
  request still reads `BLOCKED`, and the UI offers the override as a separate, deliberate
  checkbox. Anything that *waits* for mergeable, GitHub's own auto-merge above all, therefore
  waits forever. Merge directly or not at all.
- **`bypass_mode: pull_request`, never `always`.** `always` permits a **direct push** to the
  default branch. Under `pull_request` a push is refused for every actor including the owner,
  which is the property the lifecycle depends on.
- **The required context is `ci / gate`, with the space.** A caller job invoking a reusable
  workflow publishes `<caller job> / <callee job>`, and that is the name the ruleset must match.
  Requiring a bare `gate` waits for a check that is never published — the *absent check*
  deadlock: the pull request sits blocked forever with nothing red to read.
- **The tag ruleset carries no `bypass_actors` at all**, and cannot: GitHub rejects
  `bypass_mode: pull_request` on a tag ruleset outright — *"bypass mode must not be
  'PULL_REQUEST' for tag rulesets"* — since a tag never goes through a pull request. `always`
  would be the only accepted value, and nothing here needs it: the rules block **moving and
  deleting** a tag, never **creating** one, so `release-please` cuts releases normally. Moving or
  deleting a released tag is exactly what the bad-release procedure forbids in favour of a
  forward fix, so there is no legitimate consumer for an exemption.
- **The tag pattern is `refs/tags/[0-9]*`,** matching bare SemVer tags — the ecosystem's style.
  `update` is what makes a tag immutable; `non_fast_forward` alone lets a fast-forward move slip
  through.

Applying these is an onboarding step, and it runs **after** the first push: the `pull_request`
rule would otherwise reject the very push that establishes the default branch.
