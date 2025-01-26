import pytest
from puzzle_201520 import (
    do_puzzle_part1,
    do_puzzle_part2,
)
from puzzle_201520_input import puzzleInput


@pytest.mark.parametrize(
    "input, output",
    [(130, 8), (666, 30), (123456, 3600), (7654321, 191520), (puzzleInput, 831600)],
)
def test_do_puzzle_part1(input, output):
    assert do_puzzle_part1(input) == output


@pytest.mark.parametrize("input, output", [(puzzleInput, 884520)])
def test_do_puzzle_part2(input, output):
    assert do_puzzle_part2(input) == output
