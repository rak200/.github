# Rulesets

The canonical protection for every rak200 repository, committed so it is versioned and
reproducible rather than clicked. Applied per repo — `rak200` is a personal account, and
organization rulesets need an organization.

```bash
gh api -X POST repos/rak200/<repo>/rulesets --input rulesets/branch.json
gh api -X POST repos/rak200/<repo>/rulesets --input rulesets/tag.json
```

```bash
scripts/check-rulesets.sh rak200/<repo>            # read it back, by COMPARISON
scripts/check-rulesets.sh rak200/utils rak200/ui   # …or sweep the estate
```

**The read-back is a comparison, not a listing.** What used to stand here printed
`{name,target,enforcement}` — it proved two rulesets existed and nothing about what they contained.
That is how the four parameters below sat on the rule deciding who may merge, unchosen and
unreported, until one was found by accident and a fourth was found by the checker on its first run.

`check-rulesets.sh` compares in **both** directions: a declared parameter whose value differs, and
**a parameter GitHub applied that this file never declared**. It lives here, beside the JSON it
grades, so the declaration and the check ship as one thing and no network call can disagree with
the copy being read. It is **not** a required check — a platform default arrives everywhere at
once, and a gate on it reddens every repository simultaneously for something absent from the pull
request.

Each of the following was earned by a measurement:

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
- **GitHub injects parameters this file does not send, so everything is declared explicitly.**
  Measured 2026-08-24 on a throwaway ruleset: a `POST` of five `pull_request` parameters is
  stored as **eight**, and a `PUT` of the same five re-injects the extras rather than removing
  them. **A ruleset cannot be returned to its declaration by re-applying the file** — the only
  lever is to declare the value wanted, which does stick. Four were arriving undeclared and are
  now named here:
  - `allowed_merge_methods` defaulted to `["merge","squash","rebase"]` and is declared
    `["squash"]`. It was never an open door — `allow_merge_commit` and `allow_rebase_merge` are
    `false` in the repository settings, and the narrower constraint wins — but **two layers were
    stating the same policy and disagreeing**, with the disagreeing one undeclared.
  - `require_extra_approval_for_unattributed_changes` defaulted to `true` and is kept `true`.
    RFC 0017 `E.29` measured that it does not fire on a commit whose git author matches no
    account, so it grades nothing today; it is kept because it costs nothing and may matter once
    a second identity exists.
  - `required_reviewers` (`[]`) and `do_not_enforce_on_create` (`false`) are declared at their
    defaults, so that a future change to either is a diff rather than a silence.

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
