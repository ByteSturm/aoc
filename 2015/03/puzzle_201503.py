from puzzle_201503_input import puzzleInput


def countHousesWithAtLeastOneVisit(input: str):
    x = y = 0
    visitedHouses: set[str] = {coordinates(x, y)}
    for char in input:
        if char == "^":
            y += 1
        elif char == ">":
            x += 1
        elif char == "v":
            y -= 1
        elif char == "<":
            x -= 1
        visitedHouses.add(coordinates(x, y))
    return len(visitedHouses)


def coordinates(x: int, y: int) -> str:
    return f"{x},{y}"


def do_puzzle_part2(input):
    return None


print(countHousesWithAtLeastOneVisit(puzzleInput))
print(do_puzzle_part2(puzzleInput))
