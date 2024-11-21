import pytest
from puzzle_201503 import countHousesWithAtLeastOneVisit, do_puzzle_part2
from puzzle_201503_input import puzzleInput


@pytest.mark.parametrize(
    "input, output", [(">", 2), ("^>v<", 4), ("^v^v^v^v^v", 2), (puzzleInput, 2081)]
)
def test_countHousesWithAtLeastOneVisit(input, output):
    assert countHousesWithAtLeastOneVisit(input) == output


@pytest.mark.parametrize("input, output", [("dummy-input", 0), (puzzleInput, None)])
def test_do_puzzle_part2(input, output):
    assert do_puzzle_part2(input) == output
