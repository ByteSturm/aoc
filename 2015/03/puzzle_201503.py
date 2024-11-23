from puzzle_201503_input import puzzleInput


def countHousesWithAtLeastOneVisit(input: str):
    coordinates = (0, 0)
    visitedHouses: set[tuple[int, int]] = {coordinates}
    for char in input:
        coordinates = move(coordinates, char)
        visitedHouses.add(coordinates)
    return len(visitedHouses)


def move(coordinates: tuple[int, int], moveAction: chr) -> tuple[int, int]:
    x, y = coordinates
    if moveAction == "^":
        y += 1
    elif moveAction == ">":
        x += 1
    elif moveAction == "v":
        y -= 1
    elif moveAction == "<":
        x -= 1
    return (x, y)


def countHousesWithAtLeastOneVisitRoboVersion(input: str):
    santa = (0, 0)
    roboSanta = (0, 0)
    visitedHouses: set[tuple[int, int]] = {santa}
    for index, char in enumerate(input):
        if index % 2 == 0:
            santa = move(santa, char)
            visitedHouses.add(santa)
        else:
            roboSanta = move(roboSanta, char)
            visitedHouses.add(roboSanta)
    return len(visitedHouses)


if __name__ == "__main__":
    print(countHousesWithAtLeastOneVisit(puzzleInput))
    print(countHousesWithAtLeastOneVisitRoboVersion(puzzleInput))
