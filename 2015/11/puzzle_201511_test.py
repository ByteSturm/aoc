import pytest
from puzzle_201511 import (
    nextPassword,
    ruleAtLeastThreeAscendingCharacters,
    ruleNoForbiddenLetters,
    ruleAtLeastTwoDifferentPairs,
    increment,
)
from puzzle_201511_input import puzzleInput


@pytest.mark.parametrize(
    "input, output",
    [
        ("abcdefgh", "abcdffaa"),
        ("ghijklmn", "ghjaabcc"),
        ("vzbxxyzz", "vzcaabcc"),
        (puzzleInput, "vzbxxyzz"),
    ],
)
def test_nextPassword(input, output):
    assert nextPassword(input) == output


@pytest.mark.parametrize(
    "input, output",
    [
        ("hijklmmn", True),
        ("abbceffg", False),
        ("abbcegjk", False),
        ("ghjaabcc", True),
    ],
)
def test_ruleAtLeastThreeAscendingCharacters(input, output):
    assert ruleAtLeastThreeAscendingCharacters(input) == output


@pytest.mark.parametrize(
    "input, output",
    [
        ("hijklmmn", False),
        ("abbceffg", True),
        ("abbcegjk", True),
        ("hijklmmn", False),
    ],
)
def test_ruleNoForbiddenLetters(input, output):
    assert ruleNoForbiddenLetters(input) == output


@pytest.mark.parametrize(
    "input, output",
    [
        ("himmjklmmn", False),
        ("hijklmmn", False),
        ("abbceffg", True),
        ("abbcegjk", False),
        ("hijklmmmn", False),
    ],
)
def test_ruleAtLeastTwoDifferentPairs(input, output):
    assert ruleAtLeastTwoDifferentPairs(input) == output


@pytest.mark.parametrize(
    "input, output",
    [
        ("a", "b"),
        ("z", "aa"),
        ("zz", "aaa"),
        ("fefza", "fefzb"),
        ("fefzz", "fegaa"),
    ],
)
def test_increment(input, output):
    assert increment(input) == output
