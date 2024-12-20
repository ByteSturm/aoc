import pytest
from puzzle_201501 import getFloor, whenFirstTimeInBasement
from puzzle_201501_input import puzzleInput


@pytest.mark.parametrize(
    "input, output",
    [
        ("(())", 0),
        ("()()", 0),
        ("(((", 3),
        ("(()(()(", 3),
        ("))(((((", 3),
        ("())", -1),
        ("))(", -1),
        (")))", -3),
        (")())())", -3),
        (puzzleInput, 280),
    ],
)
def test_getFloor(input, output):
    assert getFloor(input) == output


@pytest.mark.parametrize(
    "input, output",
    [
        (")", 1),
        ("()())", 5),
        ("())", 3),
        ("))(", 1),
        (puzzleInput, 1797),
    ],
)
def test_whenFirstTimeInBasement(input, output):
    assert whenFirstTimeInBasement(input) == output
