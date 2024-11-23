import pytest
from puzzle_201506 import (
    setupGrid,
    setupGridv2,
    parseInput,
    ParsedInput,
    Mode,
    executeCommand,
)
from puzzle_201506_input import puzzleInput


@pytest.mark.parametrize(
    "input, grid, output",
    [
        (["turn on 0,0 through 1,1"], [[-1, -1], [-1, -1]], 4),
        (["turn off 0,0 through 1,1"], [[1, 1], [1, 1]], 0),
        (["toggle 0,0 through 1,1"], [[-1, 1], [1, -1]], 2),
        (["toggle 0,0 through 1,0"], [[-1, -1], [-1, -1]], 2),
        (
            [
                "turn on 0,0 through 1,2",
                "toggle 1,1 through 2,2",
                "turn off 0,2 through 2,2",
            ],
            [[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]],
            4,
        ),
        (
            ["turn on 0,0 through 999,999"],
            [[-1] * 1000 for _ in range(1000)],
            1000000,
        ),
        (["toggle 0,0 through 999,0"], [[1] * 1000 for _ in range(1000)], 999000),
        (
            ["turn off 499,499 through 500,500"],
            [[-1] * 1000 for _ in range(1000)],
            0,
        ),
        (
            ["turn off 499,499 through 500,500"],
            [[1] * 1000 for _ in range(1000)],
            999996,
        ),
        (puzzleInput, [[-1] * 1000 for _ in range(1000)], 377891),
    ],
)
def test_setupGrid(input, grid, output):
    assert setupGrid(input, grid) == output


@pytest.mark.parametrize(
    "input, grid, output",
    [
        (["turn on 0,0 through 0,0"], [[0] * 1000 for _ in range(1000)], 1),
        (["toggle 0,0 through 999,999"], [[0] * 1000 for _ in range(1000)], 2000000),
        (puzzleInput, [[0] * 1000 for _ in range(1000)], 14110788),
    ],
)
def test_setupGridv2(input, grid, output):
    assert setupGridv2(input, grid) == output


@pytest.mark.parametrize(
    "input, output",
    [
        ("turn on 0,0 through 999,999", ParsedInput(Mode.ON, 0, 0, 999, 999)),
        ("toggle 0,0 through 999,0", ParsedInput(Mode.TOGGLE, 0, 0, 999, 0)),
        ("turn off 499,499 through 500,500", ParsedInput(Mode.OFF, 499, 499, 500, 500)),
    ],
)
def test_parseInput(input, output):
    assert parseInput(input) == output


@pytest.mark.parametrize(
    "inputCommand, inputGrid, output",
    [
        (
            ParsedInput(Mode.ON, 0, 0, 1, 1),
            [[-1, -1], [-1, -1]],
            [[1, 1], [1, 1]],
        ),
        (
            ParsedInput(Mode.TOGGLE, 0, 0, 1, 1),
            [[-1, 1], [1, -1]],
            [[1, -1], [-1, 1]],
        ),
        (
            ParsedInput(Mode.OFF, 0, 0, 1, 1),
            [[1, 1], [1, 1]],
            [[-1, -1], [-1, -1]],
        ),
    ],
)
def test_executeCommand(inputCommand, inputGrid, output):
    executeCommand(inputGrid, inputCommand)
    assert inputGrid == output
