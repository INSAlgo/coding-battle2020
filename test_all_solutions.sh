#!/usr/bin/env bash

set -euo pipefail

while IFS= read -r -d '' problem; do
    echo "Testing solutions in: ${problem}"

    while IFS= read -r -d '' solution; do
        ./test_solution.sh "${solution}"
    done < <(find "${problem}" -type f -print0)

done < <(find . -name 'sol' -type d -print0)
