#!/usr/bin/env bash
current_year=$(date +"%Y")
current_day=$(date +"%d")
year=${1:-${current_year}}
day=$(printf "%02d" ${2:-${current_day}})

echo "puzzleInput=None" > "${year}/${day}/puzzle_${year}${day}_input.py"

cat <<EOT > "${year}/${day}/puzzle_${year}${day}_test.py"
import pytest
from puzzle_${year}${day} import do_puzzle_part1, do_puzzle_part2
from puzzle_${year}${day}_input import puzzleInput

@pytest.mark.parametrize("input, output", [
    ("dummy-input",0),
    (puzzleInput, None)
])
def test_do_puzzle_part1(input, output):
    assert do_puzzle_part1(input) == output

@pytest.mark.parametrize("input, output", [
    ("dummy-input",0),
    (puzzleInput, None)
])
def test_do_puzzle_part2(input, output):
    assert do_puzzle_part2(input) == output
EOT

cat << EOT > "${year}/${day}/puzzle_${year}${day}.py"
from puzzle_${year}${day}_input import puzzleInput

def do_puzzle_part1(input):
    return None

def do_puzzle_part2(input):
    return None

if __name__ == "__main__":
    print(do_puzzle_part1(puzzleInput))
    print(do_puzzle_part2(puzzleInput))
EOT
