# Rulesets

The canonical protection for every rak200 repository, committed so it is versioned and
reproducible rather than clicked. Applied per repo — `rak200` is a personal account, and
organization rulesets need an organization.

```bash
gh api -X POST repos/rak200/<repo>/rulesets --input rulesets/branch.json
gh api -X POST repos/rak200/<repo>/rulesets --input rulesets/tag.json
gh api repos/rak200/<repo>/rulesets --jq '[.[] | {name,target,enforcement}]'   # read it back
```

Three fields are load-bearing and each was earned by a measurement:

- **`bypass_actors` must be declared.** A repository admin is *not* implicitly exempt; without
  this entry even `--admin` cannot merge the Release PR, whose required check is absent by
  construction.
- **A bypass is granted per ruleset, never per rule.** There is no way to exempt an actor from
  the review requirement without exempting it from `ci / gate` in the same stroke. Any future
  exemption has to be weighed as that, and the branch rules stay in one ruleset until something
  needs otherwise.
- **A bypass does not make a pull request mergeable.** It lets an actor merge one that is not.
  GitHub computes mergeability without consulting `bypass_actors` at all — a bypassed pull
  request still reads `BLOCKED`, and the UI offers the override as a separate, deliberate
  checkbox. Anything that *waits* for mergeable, GitHub's own auto-merge included, therefore
  waits forever on such a pull request.
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
