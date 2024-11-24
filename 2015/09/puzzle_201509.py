from itertools import permutations
import re
from collections import defaultdict
from puzzle_201509_input import puzzleInput


def parseInput(input: list[str]) -> dict[str, dict[str, int]]:
    allEdges: dict[str, dict[str, int]] = defaultdict(dict)
    for line in input:
        result = re.search(r"(?P<start>\w+) to (?P<end>\w+) = (?P<distance>\d+)", line)
        start = result.group("start")
        end = result.group("end")
        distance = int(result.group("distance"))
        allEdges[start][end] = distance
        allEdges[end][start] = distance
    return allEdges


def findShortestPathPermutation(input: list[str]):
    allEdges = parseInput(input)

    allNodes = list(allEdges.keys())

    shortestPathLength = 999999999
    for permutation in permutations(allNodes):
        currentLength = 0
        for idx in range(len(permutation) - 1):
            currentLength += allEdges.get(permutation[idx]).get(permutation[idx + 1])
        if currentLength < shortestPathLength:
            shortestPathLength = currentLength

    return shortestPathLength


def findLongestPathPermutation(input: list[str]):
    allEdges = parseInput(input)

    allNodes = list(allEdges.keys())

    longestPathLength = 0
    for permutation in permutations(allNodes):
        currentLength = 0
        for idx in range(len(permutation) - 1):
            currentLength += allEdges.get(permutation[idx]).get(permutation[idx + 1])
        if currentLength > longestPathLength:
            longestPathLength = currentLength

    return longestPathLength


if __name__ == "__main__":
    print(findShortestPathPermutation(puzzleInput))
    print(findLongestPathPermutation(puzzleInput))
