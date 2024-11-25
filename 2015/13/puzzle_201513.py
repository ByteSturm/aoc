import collections
from itertools import permutations
import re
from puzzle_201513_input import puzzleInput


def findBestSeating(input: list[str]):
    seatPairValues = parseInput(input)
    return findHighestSeatingValue(seatPairValues)


def findBestSeatingv2(input: list[str]):
    seatPairValues = parseInput(input)
    persons = list(seatPairValues.keys())
    for person in persons:
        seatPairValues["me"][person] = 0
        seatPairValues[person]["me"] = 0
    return findHighestSeatingValue(seatPairValues)


def findHighestSeatingValue(seatPairValues: dict[str, dict[str, int]]) -> int:
    biggestSum = 0
    for permutation in permutations(seatPairValues.keys()):
        currentSum = 0
        for idx in range(len(permutation)):
            person1 = permutation[idx % len(permutation)]
            person2 = permutation[(idx + 1) % len(permutation)]
            currentSum = (
                currentSum
                + seatPairValues[person1][person2]
                + seatPairValues[person2][person1]
            )
        if currentSum > biggestSum:
            biggestSum = currentSum
    return biggestSum


def parseInput(input: list[str]) -> dict[str, dict[str, int]]:
    seatPairValues: dict[str, dict[str, int]] = collections.defaultdict(dict)
    for line in input:
        parsed = parseLine(line)
        seatPairValues[parsed[0]][parsed[1]] = parsed[2]
    return seatPairValues


def parseLine(line: str) -> tuple[str, str, int]:
    searchResult = re.search(
        r"(?P<person1>\w+) would (?P<sign>gain|lose) (?P<happiness>\d+) happiness units by sitting next to (?P<person2>\w+)",
        line,
    )
    sign = 1 if searchResult.group("sign") == "gain" else -1
    return (
        searchResult.group("person1"),
        searchResult.group("person2"),
        int(searchResult.group("happiness")) * sign,
    )


if __name__ == "__main__":
    print(findBestSeating(puzzleInput))
    print(findBestSeatingv2(puzzleInput))
