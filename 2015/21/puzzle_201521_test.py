import pytest
from puzzle_201521 import Character, do_puzzle_part1, do_puzzle_part2, simulate_fight
from puzzle_201521_input import puzzleInput


@pytest.mark.parametrize(
    "player, boss, output",
    [
        (Character(8, 5, 5), Character(12, 7, 2), True),
        (
            Character(100, 0, 0),
            Character(puzzleInput["hp"], puzzleInput["damage"], puzzleInput["armor"]),
            False,
        ),
        (
            Character(100, 7, 2),
            Character(puzzleInput["hp"], puzzleInput["damage"], puzzleInput["armor"]),
            False,
        ),
    ],
)
def test_simulate_fight(player, boss, output):
    assert simulate_fight(player, boss) == output


@pytest.mark.parametrize("input, output", [(puzzleInput, 121)])
def test_do_puzzle_part1(input, output):
    assert do_puzzle_part1(input) == output


@pytest.mark.parametrize("input, output", [("dummy-input", 0), (puzzleInput, None)])
def test_do_puzzle_part2(input, output):
    assert do_puzzle_part2(input) == output
