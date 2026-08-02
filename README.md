# rak200/.github

The GitHub-native machinery of the rak200 ecosystem: what the platform itself reads.

| What | Where | How it reaches a repository |
| --- | --- | --- |
| Reusable CI workflows | [`.github/workflows/`](.github/workflows) | referenced by each repo's thin caller, at an exact tag |
| Branch and tag rulesets | [`rulesets/`](rulesets) | applied per repo via `gh api` at onboarding, verified by read-back |
| Issue templates, PR template | [`.github/`](.github) | inherited natively by every repo without one |
| `CONTRIBUTING`, `SECURITY`, `CODE_OF_CONDUCT` | repository root | inherited natively |

**This repository is not the baseline.** The conventions, the lifecycle document, the scaffold
and the onboarding script live in **[rak200/workflow](https://github.com/rak200/workflow)**, which
travels into each repository as the `.rak200/` submodule. The split is deliberate: this repository
holds only what GitHub reads on its own, so that everything *else* can be versioned and pinned per
consumer instead of silently tracking a moving target.

## The pipeline

One reusable workflow holds the pipeline; each repository carries a thin caller so the required
check keeps a stable name.

- **`base.yml`** — language-agnostic: the seeded-file conformance check, README mirror badges,
  documentation coverage, roadmap pruning, `gitleaks`, and the aggregator. A repository with no
  language calls it directly.
- **`php.yml`** — calls `base.yml`, adds the PHP matrix (`validate → install → lint → analyse →
  test → coverage floor → scanners → mutation floor`), and aggregates both in its own gate.

```yaml
jobs:
  ci:
    uses: rak200/.github/.github/workflows/php.yml@1.0.0   # exact tag, never a moving alias
    with:
      php-versions: '["8.4", "8.5"]'
```

**The required check is `ci / gate`, and the name is not incidental.** A caller job invoking a
reusable workflow publishes `<caller job> / <callee job>`, and that name fans out per matrix cell
— so requiring a matrix check breaks at the next version bump. Two names are therefore
conventions: the caller's job is `ci`, and every reusable workflow's last job is `gate`.

Two lines inside the aggregator are rules rather than style, and both were earned by measuring a
gate that looked green and enforced nothing: **`if: always()`** (omit it and a skipped required
check counts as *satisfied*) and **equality with `success`** (inequality with `failure` lets a
cancelled run through).

## Versioning

Tags are bare SemVer (`1.0.0`, no `v`). Consumers pin an exact tag: pipeline releases and
conventions releases have different cadences and must not couple.
