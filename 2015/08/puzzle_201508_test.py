import pytest
from puzzle_201508 import (
    do_puzzle_part1,
    do_puzzle_part2,
    calculateLengths,
    calculateLengths,
)
from puzzle_201508_input import puzzleInput


@pytest.mark.parametrize(
    "input, output",
    [
        (r'""', {"code": 2, "string": 0}),
        (r'"abc"', {"code": 5, "string": 3}),
        (r'"aaa\"aaa"', {"code": 10, "string": 7}),
        (r'"\x27"', {"code": 6, "string": 1}),
        (r'"\\"', {"code": 4, "string": 1}),
        (r'"\xa8br\x8bjr\""', {"code": 16, "string": 7}),
        (r'"bvm\x28aa\\\\\"pywuhaniox\\z\\hbp\xd7mold"', {"code": 43, "string": 30}),
    ],
)
def test_calculateLengths(input, output):
    assert calculateLengths(input) == output


def test_do_puzzle_part1():
    assert do_puzzle_part1(puzzleInput) == 1371


@pytest.mark.parametrize("input, output", [("dummy-input", 0), (puzzleInput, None)])
def test_do_puzzle_part2(input, output):
    assert do_puzzle_part2(input) == output
