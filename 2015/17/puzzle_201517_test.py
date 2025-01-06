import pytest
from puzzle_201517 import do_puzzle_part1, do_puzzle_part2
from puzzle_201517_input import puzzleInput


@pytest.mark.parametrize(
    "liters, buckets, combinations",
    [
        (25, [20, 15, 10, 5, 5], 4),
        (150, puzzleInput, 1304),
    ],
)
def test_do_puzzle_part1(liters, buckets, combinations):
    assert do_puzzle_part1(liters, buckets) == combinations


@pytest.mark.parametrize(
    "liters, buckets, combinations",
    [
        (25, [20, 15, 10, 5, 5], 3),
        (150, puzzleInput, 18),
    ],
)
def test_do_puzzle_part2(liters, buckets, combinations):
    assert do_puzzle_part2(liters, buckets) == combinations
