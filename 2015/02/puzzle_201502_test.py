import pytest
from puzzle_201502 import calculateTotalNeededWrappingPaper, calculateTotalRibbonNeeded
from puzzle_201502_input import puzzleInput


@pytest.mark.parametrize(
    "input, output",
    [
        (["2x3x4"], 58),
        (["1x1x10"], 43),
        (puzzleInput, 1598415),
    ],
)
def test_calculateTotalNeededWrappingPaper(input, output):
    assert calculateTotalNeededWrappingPaper(input) == output


@pytest.mark.parametrize(
    "input, output",
    [
        (["2x3x4"], 34),
        (["1x1x10"], 14),
        (puzzleInput, 3812909),
    ],
)
def test_do_puzzle_part2(input, output):
    assert calculateTotalRibbonNeeded(input) == output
