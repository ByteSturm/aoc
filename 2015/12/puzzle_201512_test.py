import pytest
from puzzle_201512 import sumNumbersInComplexObject
from puzzle_201512_input import puzzleInput


@pytest.mark.parametrize(
    "input, output",
    [
        ([1, 2, 3], 6),
        ({"a": 2, "b": 4}, 6),
        ([[[3]]], 3),
        ({"a": {"b": 4}, "c": -1}, 3),
        ({"a": [-1, 1]}, 0),
        ([-1, {"a": 1}], 0),
        ([], 0),
        ({}, 0),
        (puzzleInput, 111754),
    ],
)
def test_sumNumbersInComplexObject(input, output):
    assert sumNumbersInComplexObject(input) == output


@pytest.mark.parametrize(
    "input, output",
    [
        ([1, 2, 3], 6),
        ({"a": 2, "b": 4}, 6),
        ([[[3]]], 3),
        ({"a": {"b": 4}, "c": -1}, 3),
        ({"a": [-1, 1]}, 0),
        ([-1, {"a": 1}], 0),
        ([], 0),
        ({}, 0),
        ([1, {"c": "red", "b": 2}, 3], 4),
        ({"d": "red", "e": [1, 2, 3, 4], "f": 5}, 0),
        ([1, "red", 5], 6),
        (puzzleInput, 65402),
    ],
)
def test_sumNumbersInComplexObjectPart2(input, output):
    assert sumNumbersInComplexObject(input, True) == output
