"""Emit every named step of the reusable workflows as `workflow<TAB>job<TAB>step<TAB>condition`.

The condition is the step's `if:` verbatim, comment stripped, empty when unconditional. It is
part of the identity of a gate and not decoration: an `if:` decides whether the step runs at
all, so `mutation — floor (full)`, conditioned on workflow_dispatch, never runs on a pull
request. A canary fired through a pull request cannot reach it, and no list of step names
could say so.

Deliberately a line scanner rather than a YAML parse: pyyaml is not present on this estate's
runners, and a derivation must not depend on a package that may be absent where it runs.
"""
import re
import sys
import pathlib


def steps(path):
    job = None
    lines = path.read_text().split("\n")
    for i, line in enumerate(lines):
        m = re.match(r"^  ([A-Za-z_][\w-]*):\s*$", line)
        if m:
            job = m.group(1)
            continue
        m = re.match(r"^(\s*)- name:\s*(.+?)\s*$", line)
        if not m:
            continue
        indent = len(m.group(1))
        name = m.group(2).strip().strip("\"'")
        condition = ""
        for nxt in lines[i + 1:]:
            # the step block ends at the next line indented no further than the `- name:`
            if nxt.strip() and not nxt.startswith(" " * (indent + 2)):
                break
            m2 = re.match(r"^\s*if:\s*(.+?)\s*$", nxt)
            if m2 and not condition:
                condition = re.sub(r"\s+#.*$", "", m2.group(1)).strip()
        yield path.stem, job or "?", name, condition


for arg in sys.argv[1:]:
    for row in steps(pathlib.Path(arg)):
        print("\t".join(row))
