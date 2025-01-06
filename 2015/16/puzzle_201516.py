from puzzle_201516_input import puzzleInput
import re

testResult = {
    "name": None,
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1,
}


def parseAunt(line: str) -> dict[str, int]:
    aunt: dict[str, int] = dict()
    searchResult = re.search(r"Sue (?P<name>\d+): (?P<properties>.*)", line)
    properties = searchResult.group("properties").split(",")
    aunt.setdefault("name", int(searchResult.group("name")))
    for prop in properties:
        propSearchResult = re.search(r"(?P<key>\w+): (?P<value>\d+)", prop)
        aunt.setdefault(
            propSearchResult.group("key"), int(propSearchResult.group("value"))
        )
    return aunt


def doesMatch(aunt: dict[str, int]) -> bool:
    matches = True
    testResult["name"] = aunt["name"]
    for key in aunt:
        matches = matches and aunt[key] == testResult[key]
    return matches


def do_puzzle_part1(input: list[str]):
    aunts = list(map(parseAunt, input))
    filteredAunts = list(filter(doesMatch, aunts))
    return filteredAunts


def doesMatchV2(aunt: dict[str, int]) -> bool:
    matches = True
    testResult["name"] = aunt["name"]
    for key in aunt:
        if key == "cats" or key == "trees":
            matches = matches and aunt[key] > testResult[key]
        elif key == "pomeranians" or key == "goldfish":
            matches = matches and aunt[key] < testResult[key]
        else:
            matches = matches and aunt[key] == testResult[key]
    return matches


def do_puzzle_part2(input: list[str]):
    aunts = list(map(parseAunt, input))
    filteredAunts = list(filter(doesMatchV2, aunts))
    return filteredAunts


if __name__ == "__main__":
    print(do_puzzle_part1(puzzleInput))
    print(do_puzzle_part2(puzzleInput))
