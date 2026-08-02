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
- **`bypass_mode: pull_request`, never `always`.** `always` permits a **direct push** to the
  default branch. Under `pull_request` a push is refused for every actor including the owner,
  which is the property the lifecycle depends on.
- **The tag pattern is `refs/tags/[0-9]*`,** matching bare SemVer tags — the ecosystem's style.
  `update` is what makes a tag immutable; `non_fast_forward` alone lets a fast-forward move slip
  through.

Applying these is an onboarding step, and it runs **after** the first push: the `pull_request`
rule would otherwise reject the very push that establishes the default branch.
