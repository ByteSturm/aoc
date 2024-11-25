import pytest
from puzzle_201513 import findBestSeating, parseLine
from puzzle_201513_input import puzzleInput


@pytest.mark.parametrize(
    "input, output",
    [
        (
            [
                "Alice would gain 54 happiness units by sitting next to Bob.",
                "Alice would lose 79 happiness units by sitting next to Carol.",
                "Alice would lose 2 happiness units by sitting next to David.",
                "Bob would gain 83 happiness units by sitting next to Alice.",
                "Bob would lose 7 happiness units by sitting next to Carol.",
                "Bob would lose 63 happiness units by sitting next to David.",
                "Carol would lose 62 happiness units by sitting next to Alice.",
                "Carol would gain 60 happiness units by sitting next to Bob.",
                "Carol would gain 55 happiness units by sitting next to David.",
                "David would gain 46 happiness units by sitting next to Alice.",
                "David would lose 7 happiness units by sitting next to Bob.",
                "David would gain 41 happiness units by sitting next to Carol.",
            ],
            330,
        ),
        (puzzleInput, 618),
    ],
)
def test_findBestSeating(input, output):
    assert findBestSeating(input) == output


@pytest.mark.parametrize(
    "input, output",
    [
        (
            "Alice would gain 54 happiness units by sitting next to Bob.",
            ("Alice", "Bob", 54),
        ),
        (
            "Alice would lose 79 happiness units by sitting next to Carol.",
            ("Alice", "Carol", -79),
        ),
        (
            "Alice would lose 2 happiness units by sitting next to David.",
            ("Alice", "David", -2),
        ),
        (
            "Bob would gain 83 happiness units by sitting next to Alice.",
            ("Bob", "Alice", 83),
        ),
        (
            "Bob would lose 7 happiness units by sitting next to Carol.",
            ("Bob", "Carol", -7),
        ),
        (
            "Bob would lose 63 happiness units by sitting next to David.",
            ("Bob", "David", -63),
        ),
        (
            "Carol would lose 62 happiness units by sitting next to Alice.",
            ("Carol", "Alice", -62),
        ),
        (
            "Carol would gain 60 happiness units by sitting next to Bob.",
            ("Carol", "Bob", 60),
        ),
        (
            "Carol would gain 55 happiness units by sitting next to David.",
            ("Carol", "David", 55),
        ),
        (
            "David would gain 46 happiness units by sitting next to Alice.",
            ("David", "Alice", 46),
        ),
        (
            "David would lose 7 happiness units by sitting next to Bob.",
            ("David", "Bob", -7),
        ),
        (
            "David would gain 41 happiness units by sitting next to Carol.",
            ("David", "Carol", 41),
        ),
    ],
)
def test_parseLine(input, output):
    assert parseLine(input) == output
