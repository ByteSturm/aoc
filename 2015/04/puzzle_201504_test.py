import pytest
from puzzle_201504 import getLowestNumber, do_puzzle_part2
from puzzle_201504_input import puzzleInput


@pytest.mark.parametrize(
    "input, output", [("abcdef", 609043), ("pqrstuv", 1048970), (puzzleInput, 282749)]
)
def test_do_puzzle_part1(input, output):
    assert getLowestNumber(input) == output


@pytest.mark.parametrize("input, output", [("dummy-input", 0), (puzzleInput, None)])
def test_do_puzzle_part2(input, output):
    assert do_puzzle_part2(input) == output
