import pytest
from puzzle_201504 import getLowestNumberForHashWithFiveZeroes
from puzzle_201504_input import puzzleInput


@pytest.mark.parametrize(
    "input, output", [("abcdef", 609043), ("pqrstuv", 1048970), (puzzleInput, 282749)]
)
def test_getLowestNumber(input, output):
    assert getLowestNumberForHashWithFiveZeroes(input) == output
