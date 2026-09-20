"""Grade this repository's workflows against the non-negotiables about their SHAPE.

Three rules from `CONVENTIONS.md` §Non-negotiables, each earned by a gate that looked green and
enforced nothing:

  2  an aggregator carries `if: always()` and compares for EQUALITY with success — a skipped
     required check counts as satisfied, and `!= 'failure'` lets a cancelled run through
  3  a workflow producing a required check carries no `paths:` filter — a filtered run publishes
     NO check, and the pull request waits forever on a context that will never arrive
  4  a pipeline is audited on a step's `outcome`, never its `conclusion` — `continue-on-error`
     relabels a failure as success in `conclusion` alone

A line scanner rather than a YAML parse, for the reason `gates-extract.py` gives: pyyaml is not
present on this estate's runners, and a check must not depend on a package that may be absent
where it runs. Full-line comments are dropped first, so a comment ABOUT `conclusion` — there is
one in release.yml — is not read as a use of it.

Reach: the workflows in this repository, which is where the pipeline lives. A consumer's caller is
a seeded file, so a `paths:` filter added to one is caught as seed drift instead; a consumer's own
other workflows are graded by nobody.
"""

import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
WORKFLOWS = sorted((ROOT / ".github" / "workflows").glob("*.yml"))

JOB = re.compile(r"^  ([A-Za-z_][\w-]*):\s*$")
PATHS = re.compile(r"^\s*paths(-ignore)?:")
CONCLUSION = re.compile(r"steps\.[A-Za-z_][\w-]*\.conclusion")
SUCCESS = re.compile(r"[=]=?\s*[\"']success[\"']")
NOT_FAILURE = re.compile(r"!=\s*[\"']failure[\"']")

problems = []


def problem(path, line, message):
    problems.append(f"::error file={path},line={line}::{message}")


def uncommented(path):
    """Every line with its 1-based number, minus the full-line comments."""
    return [
        (n, line)
        for n, line in enumerate(path.read_text().split("\n"), 1)
        if not re.match(r"^\s*#", line)
    ]


def jobs(lines):
    """(name, [(lineno, text), …]) per top-level job, in file order."""
    found, name, block = [], None, []
    for n, line in lines:
        match = JOB.match(line)
        if match:
            if name:
                found.append((name, block))
            name, block = match.group(1), []
            continue
        if name:
            block.append((n, line))
    if name:
        found.append((name, block))
    return found


aggregators = 0
for workflow in WORKFLOWS:
    rel = workflow.relative_to(ROOT)
    lines = uncommented(workflow)

    for n, line in lines:
        if PATHS.match(line):
            problem(rel, n, "a workflow producing a required check carries no `paths:` filter: a filtered run publishes no check at all, and the pull request waits forever")
        if CONCLUSION.search(line):
            problem(rel, n, "audit a step on its `outcome`, never its `conclusion` — `continue-on-error` relabels a failure as success in `conclusion` alone")

    for name, block in jobs(lines):
        if name != "gate":
            continue
        aggregators += 1
        start = block[0][0] if block else 1
        condition = next((line for _, line in block if re.match(r"^    if:", line)), "")
        if "always()" not in condition:
            problem(rel, start, "the `gate` job carries no `always()` in its `if:` — without it the gate is skipped when a needed job fails, and a skipped required check counts as satisfied")
        text = "\n".join(line for _, line in block)
        if not SUCCESS.search(text):
            problem(rel, start, "the `gate` job compares nothing with `success` — an aggregator decides by equality with success, or it decides nothing")
        if NOT_FAILURE.search(text):
            problem(rel, start, "the `gate` job compares with `!= 'failure'` — that lets a cancelled run through; compare for equality with `success`")

if not WORKFLOWS:
    print("::error::no workflows found — this check graded nothing", file=sys.stderr)
    sys.exit(1)
if not aggregators:
    print("::error::no `gate` job found in any workflow — the aggregator rules graded nothing", file=sys.stderr)
    sys.exit(1)

for line in problems:
    print(line, file=sys.stderr)
print(f"checked {len(WORKFLOWS)} workflow(s), {aggregators} aggregator(s): "
      f"{'shape holds' if not problems else str(len(problems)) + ' problem(s)'}")
sys.exit(1 if problems else 0)
