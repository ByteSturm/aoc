import pytest
from puzzle_201516 import do_puzzle_part1, do_puzzle_part2, parseAunt
from puzzle_201516_input import puzzleInput


@pytest.mark.parametrize(
    "input, output",
    [
        (
            "Sue 18: trees: 5, vizslas: 9, cars: 0",
            {"name": 18, "trees": 5, "vizslas": 9, "cars": 0},
        ),
        (
            "Sue 47: trees: 9, akitas: 2, vizslas: 9",
            {"name": 47, "trees": 9, "akitas": 2, "vizslas": 9},
        ),
        (
            "Sue 9999: children: 1, cats: 2, samoyeds: 3, pomeranians: 4, akitas: 5, vizslas: 6, goldfish: 7, trees: 8, cars: 9, perfumes: 10",
            {
                "name": 9999,
                "children": 1,
                "cats": 2,
                "samoyeds": 3,
                "pomeranians": 4,
                "akitas": 5,
                "vizslas": 6,
                "goldfish": 7,
                "trees": 8,
                "cars": 9,
                "perfumes": 10,
            },
        ),
    ],
)
def test_parseAunt(input, output):
    assert parseAunt(input) == output


@pytest.mark.parametrize(
    "input, output",
    [(puzzleInput, [{"name": 103, "cars": 2, "perfumes": 1, "goldfish": 5}])],
)
def test_do_puzzle_part1(input, output):
    assert do_puzzle_part1(input) == output


@pytest.mark.parametrize(
    "input, output",
    [(puzzleInput, [{"name": 405, "trees": 8, "perfumes": 1, "cars": 2}])],
)
def test_do_puzzle_part2(input, output):
    assert do_puzzle_part2(input) == output
