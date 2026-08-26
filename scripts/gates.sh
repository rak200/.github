#!/usr/bin/env sh
# The gate inventory, derived from the workflows rather than maintained beside them.
#
#   gates.sh              — check the manifest against the workflows, then print the inventory
#   gates.sh php|js       — print what one variant's repositories are actually graded by
#
# Why this exists. RFC 0017 step 5 fires "a canary per gate", and its list named eight. Step 0
# read the pipeline on 2026-08-12 and found the real number was roughly seventeen — the list
# "was about to fire eight shots at a target that has changed shape". It was reconciled by hand.
# Thirteen days later it was wrong again. Reconciling does not hold, because nothing connects
# the list to the pipeline; deriving does, because there is no list left to go stale.
#
# The check is the load-bearing half: a step present in the workflows and absent from
# gates.tsv fails this, so a gate added to the pipeline cannot escape the inventory in
# silence. A row with no step fails it too — an inventory naming a gate that no longer
# exists is a canary owed against nothing.
set -eu

here=$(cd "$(dirname "$0")/.." && pwd)
wf="$here/.github/workflows"
manifest="$here/scripts/gates.tsv"

# Compared WITH the condition, not only the name. An `if:` is what decides whether a gate
# runs at all, so a changed condition is a changed inventory — `mutation — floor (full)` runs
# on workflow_dispatch and therefore never on a pull request, which no list of names could say.
actual=$(python3 "$here/scripts/gates-extract.py" "$wf/base.yml" "$wf/php.yml" "$wf/js.yml" | sort)
declared=$(grep -v '^#' "$manifest" | awk -F'\t' 'NF>=4 {print $1"\t"$2"\t"$3"\t"$5}' | sort)

if [ "$actual" != "$declared" ]; then
  echo "gates.tsv is out of date — the manifest and the workflows disagree:" >&2
  diff <(printf '%s\n' "$declared") <(printf '%s\n' "$actual") \
    | grep -E '^[<>]' \
    | sed -e 's/^< /  declared, and not in the workflows: /' \
          -e 's/^> /  in the workflows, and not declared: /' >&2
  echo >&2
  echo "Add the row, choosing its class deliberately. A gate added to the pipeline and not" >&2
  echo "to this file is a gate nobody owes a canary for." >&2
  exit 1
fi

variant=${1:-}
case "$variant" in
  php|js)
    printf 'gates a %s repository is graded by, and what has to be true for each to run:\n\n' "$variant"
    grep -v '^#' "$manifest" | awk -F'\t' -v v="$variant" \
      '($1=="base"||$1==v) && $4=="gate" && $5 !~ /variant == .github./ {
         printf "  %-4s %-48s %s\n", $1, $3, ($5==""?"always":$5) }'
    printf '\ntotal: %s\n' "$(grep -v '^#' "$manifest" | awk -F'\t' -v v="$variant" \
      '($1=="base"||$1==v) && $4=="gate" && $5 !~ /variant == .github./' | wc -l | tr -d ' ')"
    ;;
  '')
    echo "manifest matches the workflows"
    grep -v '^#' "$manifest" | awk -F'\t' 'NF>=4 {c[$4]++} END {for (k in c) printf "  %-10s %d\n", k, c[k]}'
    for v in php js; do
      n=$(grep -v '^#' "$manifest" | awk -F'\t' -v v="$v" '($1=="base"||$1==v) && $4=="gate" && $5 !~ /variant == .github./' | wc -l | tr -d ' ')
      u=$(grep -v '^#' "$manifest" | awk -F'\t' -v v="$v" '($1=="base"||$1==v) && $4=="gate" && $5 !~ /variant == .github./ && $5==""' | wc -l | tr -d ' ')
      printf '\n  a %-3s repository is graded by %s gates, of which %s run unconditionally\n' "$v" "$n" "$u"
    done
    ;;
  *) echo "usage: gates.sh [php|js]" >&2; exit 2 ;;
esac
