# CLAUDE.md

Guidance for Claude Code when working in this repository.

@.rak200/CONVENTIONS.md

> If `.rak200/` is empty, the clone skipped its submodule:
> `git submodule update --init --recursive`. This repository has no language layer,
> so Layer 1 is the whole of its imported guidance.

## What this repository is

`rak200/.github` holds the **GitHub-native** half of the ecosystem baseline: reusable CI
workflows, the canonical ruleset JSON, and the community health files GitHub propagates on its
own. It deliberately holds nothing else — the conventions, `LIFECYCLE.md`, the scaffold and the
onboarding script live in `rak200/workflow`.

## Where the rules are

In the import above, and nowhere else here. This file restates none of them: a rule written only in
a `CLAUDE.md` binds nobody, because a human maintainer never opens one.

The ones this repository is asked to break most often are `CONVENTIONS.md` §The pipeline (the
aggregator's two lines, the scanner's three ordered steps, the exact-tag pin), §Security
(`pull_request_target`, SHA pinning, untrusted values through `env:`) and §Non-negotiables.

**How to change a workflow here without breaking a consumer is in [README.md](README.md)**, where a
human reads it.
