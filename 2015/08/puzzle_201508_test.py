import pytest
from puzzle_201508 import (
    do_puzzle_part1,
    do_puzzle_part2,
    calculateLengths,
    calculateLengthsByCounting,
    calculateLengthOfencodedString,
    calculateLengthOfencodedStringByCounting,
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
    assert calculateLengthsByCounting(input) == output


def test_do_puzzle_part1():
    assert do_puzzle_part1(puzzleInput) == 1371


@pytest.mark.parametrize(
    "input, output",
    [
        (r'""', {"code": 2, "encoded": 6}),
        (r'"abc"', {"code": 5, "encoded": 9}),
        (r'"aaa\"aaa"', {"code": 10, "encoded": 16}),
        (r'"\x27"', {"code": 6, "encoded": 11}),
        (r'"\\"', {"code": 4, "encoded": 10}),
        (r'"\xa8br\x8bjr\""', {"code": 16, "encoded": 24}),
        (r'"bvm\x28aa\\\\\"pywuhaniox\\z\\hbp\xd7mold"', {"code": 43, "encoded": 59}),
    ],
)
def test_calculateLengthOfencodedStrings(input, output):
    assert calculateLengthOfencodedString(input) == output
    assert calculateLengthOfencodedStringByCounting(input) == output


def test_do_puzzle_part2():
    assert do_puzzle_part2(puzzleInput) == 2117
