# php-min

[![PHPStan](https://img.shields.io/badge/PHPStan-level%20max-blue)](https://phpstan.org/)

A minimal PHP package, and not a real one. It exists so that `php.yml` can be run against
something inside this repository, rather than being released and discovered in a consumer's
bump pull request weeks later — the mitigation RFC 0017 names for the exact-pin decision's
one real cost.

**It is not published, not required by anything, and not a template.** A repository being
onboarded should copy the scaffold, not this.

## What it has to be

Every floor the pipeline enforces is vacuous over an empty package, so this one carries the
smallest thing that makes each of them mean something:

| verb | what makes it non-trivial here |
| --- | --- |
| `lint`, `fix` | real source for php-cs-fixer to have an opinion about |
| `analyse` | PHPStan at `level: max`, from the pinned Layer 2 config |
| `test` | a suite that covers the source |
| `coverage` | `.coverage-floor` at 100, which the suite actually meets |
| `scan` | semgrep over a package with no findings — the green half of the canary |
| `mutation` | mutants that a passing suite genuinely kills, at `minCoveredMsi: 100` |

The badge above is not decoration either: `php.yml` asserts that a README's PHPStan badge
matches the level effective in the pinned standard, so this file exercises that step.

## What it deliberately does not have

No `.rak200`, no seeds, no ROADMAP, no rulesets. Conformance is **repository**-scoped —
seed drift, submodule pin, badges, roadmap pruning, secret scanning — and none of it has a
referent inside a subdirectory. That is why the self-test passes `run-base: false` and
exercises the verbs alone: a conformance job pointed at a fixture would be measuring this
repository under another repository's variant, which is a green nobody should trust.
