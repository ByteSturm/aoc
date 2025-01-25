import pytest
from puzzle_201518 import (
    count_turned_on_neighbors,
    do_puzzle_part1,
    do_puzzle_part2,
    get_state_of,
    init_grid,
)
from puzzle_201518_input import puzzleInput


@pytest.mark.parametrize(
    "input, output",
    [
        ([], []),
        ([""], [[]]),
        (["."], [[False]]),
        (["#"], [[True]]),
        ([".", "#"], [[False], [True]]),
        (
            ["###.##..##.#.."],
            [
                [
                    True,
                    True,
                    True,
                    False,
                    True,
                    True,
                    False,
                    False,
                    True,
                    True,
                    False,
                    True,
                    False,
                    False,
                ]
            ],
        ),
    ],
)
def test_init_grid(input, output):
    assert init_grid(input) == output


@pytest.mark.parametrize(
    "input, output",
    [
        (
            (0, 0),
            True,
        ),
        (
            (-1, 0),
            False,
        ),
        (
            (0, -1),
            False,
        ),
        (
            (6, 0),
            False,
        ),
        (
            (0, 6),
            False,
        ),
        (
            (0, 3),
            False,
        ),
        (
            (3, 4),
            True,
        ),
    ],
)
def test_get_state_of(input, output):
    grid = [
        [True, True, True, False, False, False],
        [True, True, True, False, False, False],
        [False, False, False, False, False, False],
        [False, False, True, True, True, False],
        [False, False, True, True, True, False],
        [False, False, True, True, True, False],
    ]
    assert get_state_of(grid, input[0], input[1]) == output


@pytest.mark.parametrize(
    "input, output",
    [
        (
            (1, 0),
            5,
        ),
        (
            (3, 4),
            8,
        ),
    ],
)
def test_count_turned_on_neighbors(input, output):
    grid = [
        [True, True, True, False, False, False],
        [True, True, True, False, False, False],
        [False, False, False, False, False, False],
        [False, False, True, True, True, False],
        [False, False, True, True, True, False],
        [False, False, True, True, True, False],
    ]
    assert count_turned_on_neighbors(grid, input[0], input[1]) == output


@pytest.mark.parametrize(
    "input_grid, steps, output",
    [
        (
            [
                ".#.#.#",
                "...##.",
                "#....#",
                "..#...",
                "#.#..#",
                "####..",
            ],
            4,
            4,
        ),
        (puzzleInput, 100, 821),
    ],
)
def test_do_puzzle_part1(input_grid, steps, output):
    assert do_puzzle_part1(input_grid, steps) == output


@pytest.mark.parametrize(
    "input_grid, steps, output",
    [
        (
            [
                "##.#.#",
                "...##.",
                "#....#",
                "..#...",
                "#.#..#",
                "####.#",
            ],
            5,
            17,
        ),
        (puzzleInput, 100, 886),
    ],
)
def test_do_puzzle_part2(input_grid, steps, output):
    assert do_puzzle_part2(input_grid, steps) == output
