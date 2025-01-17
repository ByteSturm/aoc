import re
from functools import reduce
from enum import Enum
from dataclasses import dataclass
from puzzle_201506_input import puzzleInput


class Mode(Enum):
    ON = "turn on"
    OFF = "turn off"
    TOGGLE = "toggle"


@dataclass
class ParsedInput:
    mode: Mode
    startX: int
    startY: int
    endX: int
    endY: int


def setupGrid(input: list[str], grid: list[list[bool]]):
    for commandInput in input:
        command = parseInput(commandInput)
        executeCommand(grid, command)
    flattenedGrid = [cell for row in grid for cell in row]
    return flattenedGrid.count(1)


def setupGridv2(input: list[str], grid: list[list[bool]]):
    for commandInput in input:
        command = parseInput(commandInput)
        executeCommandv2(grid, command)
    flattenedGrid = [cell for row in grid for cell in row]
    return reduce(lambda prev, current: prev + current, flattenedGrid, 0)


def parseInput(input: str):
    captureGroups = re.search(
        r"(turn on|turn off|toggle) (\d+),(\d+) through (\d+),(\d+)", input
    )
    capturedMode = captureGroups.groups()[0]
    startX = int(captureGroups.groups()[1])
    startY = int(captureGroups.groups()[2])
    endX = int(captureGroups.groups()[3])
    endY = int(captureGroups.groups()[4])
    return ParsedInput(Mode(capturedMode), startX, startY, endX, endY)


def executeCommand(grid: list[list[bool]], command: ParsedInput) -> None:
    for x in range(command.startX, command.endX + 1, 1):
        for y in range(command.startY, command.endY + 1, 1):
            if command.mode == Mode.ON:
                grid[x][y] = 1
            elif command.mode == Mode.OFF:
                grid[x][y] = -1
            elif command.mode == Mode.TOGGLE:
                grid[x][y] = -grid[x][y]


def executeCommandv2(grid: list[list[bool]], command: ParsedInput) -> None:
    for x in range(command.startX, command.endX + 1, 1):
        for y in range(command.startY, command.endY + 1, 1):
            if command.mode == Mode.ON:
                grid[x][y] += 1
            elif command.mode == Mode.OFF:
                grid[x][y] = max(0, grid[x][y] - 1)
            elif command.mode == Mode.TOGGLE:
                grid[x][y] += 2


if __name__ == "__main__":
    print(setupGrid(puzzleInput, [[-1] * 1000 for _ in range(1000)]))
    print(setupGridv2(puzzleInput, [[0] * 1000 for _ in range(1000)]))
