import pytest
from puzzle_202401 import getTotalDistance, getSimilarity, parseInput
from puzzle_202401_input import puzzleInput


@pytest.mark.parametrize(
    "input, output",
    [
        (
            [
                "3   4",
                "4   3",
                "2   5",
                "1   3",
                "3   9",
                "3   3",
            ],
            11,
        ),
        (puzzleInput, 1765812),
    ],
)
def test_getTotalDistance(input, output):
    assert getTotalDistance(input) == output


@pytest.mark.parametrize(
    "input, output",
    [
        (
            [
                "3   4",
                "4   3",
                "2   5",
                "1   3",
                "3   9",
                "3   3",
            ],
            31,
        ),
        (puzzleInput, 20520794),
    ],
)
def test_getSimilarity(input, output):
    assert getSimilarity(input) == output


def test_parseInput():
    input = [
        "3   4",
        "4   3",
        "2   5",
        "1   3",
        "3   9",
        "3   3",
    ]
    expectedList1 = [3, 4, 2, 1, 3, 3]
    expectedList2 = [4, 3, 5, 3, 9, 3]
    (outputList1, outputList2) = parseInput(input)
    assert expectedList1 == outputList1
    assert expectedList2 == outputList2
