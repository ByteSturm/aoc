from puzzle_201518_input import puzzleInput


def init_grid(input: list[str]) -> list[list[bool]]:
    grid = list()
    for line in input:
        gridLine = list()
        grid.append(gridLine)
        for character in line:
            gridLine.append(character == "#")
    return grid


def get_state_of(grid: list[list[bool]], x: int, y: int) -> bool:
    if x < 0 or y < 0 or y >= len(grid) or x >= len(grid[0]):
        return False
    return grid[y][x]


def count_turned_on_neighbors(grid: list[list[bool]], x: int, y: int) -> int:
    return (
        (
            get_state_of(grid, x - 1, y - 1)
            + get_state_of(grid, x, y - 1)
            + get_state_of(grid, x + 1, y - 1)
        )
        + (get_state_of(grid, x - 1, y) + get_state_of(grid, x + 1, y))
        + (
            get_state_of(grid, x - 1, y + 1)
            + get_state_of(grid, x, y + 1)
            + get_state_of(grid, x + 1, y + 1)
        )
    )


def do_animation_step(oldGrid: list[list[bool]]) -> list[list[bool]]:
    newGrid = list()
    for y, line in enumerate(oldGrid):
        newLine = list()
        newGrid.append(newLine)
        for x, lightStatus in enumerate(line):
            newStatus = None
            turned_on_neighbors = count_turned_on_neighbors(oldGrid, x, y)
            turned_off_light_is_turned_on = not lightStatus and turned_on_neighbors == 3
            turned_on_light_stays_on = lightStatus and (
                turned_on_neighbors == 2 or turned_on_neighbors == 3
            )
            newStatus = turned_off_light_is_turned_on or turned_on_light_stays_on
            newLine.append(newStatus)
    return newGrid


def animate(grid: list[list[bool]], steps: int) -> list[list[bool]]:
    for _ in range(steps):
        grid = do_animation_step(grid)
    flattened_grid = [light for line in grid for light in line]
    return sum(flattened_grid)


def animate_v2(grid: list[list[bool]], steps: int) -> list[list[bool]]:
    x_max = len(grid[0]) - 1
    y_max = len(grid) - 1
    grid[0][0] = True
    grid[y_max][0] = True
    grid[0][x_max] = True
    grid[y_max][x_max] = True
    for _ in range(steps):
        grid = do_animation_step(grid)
        grid[0][0] = True
        grid[y_max][0] = True
        grid[0][x_max] = True
        grid[y_max][x_max] = True
    flattened_grid = [light for line in grid for light in line]
    return sum(flattened_grid)


def do_puzzle_part1(input_grid: list[str], animation_steps: int) -> int:
    grid = init_grid(input_grid)
    return animate(grid, animation_steps)


def do_puzzle_part2(input_grid: list[str], animation_steps: int) -> int:
    grid = init_grid(input_grid)
    return animate_v2(grid, animation_steps)


if __name__ == "__main__":
    print(do_puzzle_part1(puzzleInput, 100))
    print(do_puzzle_part2(puzzleInput, 100))
