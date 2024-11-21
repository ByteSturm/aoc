import pytest
from puzzle_201505 import isStringNice, isStringNiceV2


@pytest.mark.parametrize(
    "input, output",
    [
        ("ugknbfddgicrmopn", True),
        ("ugknbfddgicrmopn", True),
        ("aaa", True),
        ("jchzalrnumimnmhp", False),
        ("haegwjzuvuyypxyu", False),
        ("dvszwmarrgswjxmb", False),
    ],
)
def test_isStringNice(input, output):
    assert isStringNice(input) == output


@pytest.mark.parametrize(
    "input, output",
    [
        ("qjhvhtzxzqqjkmpb", True),
        ("xxyxx", True),
        ("uurcxstgmygtbstg", False),
        ("ieodomkazucvgmuy", False),
    ],
)
def test_isStringNiceV2(input, output):
    assert isStringNiceV2(input) == output
