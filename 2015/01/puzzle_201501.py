from puzzle_201501_input import puzzleInput


def getFloor(input: str) -> int:
    floor = 0
    for char in input:
        floor = move(char, floor)
    return floor


def move(char: str, floor: int) -> int:
    if char == "(":
        floor += 1
    elif char == ")":
        floor -= 1
    return floor


def whenFirstTimeInBasement(input: str) -> int:
    floor = 0
    step = 0
    reachedBasement = False
    while not reachedBasement:
        floor = move(input[step], floor)
        step += 1
        reachedBasement = floor == -1
    return step


if __name__ == "__main__":
    print(getFloor(puzzleInput))
    print(whenFirstTimeInBasement(puzzleInput))
