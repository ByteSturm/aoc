import pytest
from puzzle_201510 import do_puzzle_part1, do_puzzle_part2, lookAndSay
from puzzle_201510_input import puzzleInput


@pytest.mark.parametrize(
    "input, output",
    [
        ("1", "11"),
        ("11", "21"),
        ("21", "1211"),
        ("1211", "111221"),
        ("111221", "312211"),
    ],
)
def test_lookAndSay(input, output):
    assert lookAndSay(input) == output
