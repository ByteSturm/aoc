from puzzle_202401_input import puzzleInput


def parseInput(input: list[str]) -> tuple[list[str], list[str]]:
    list1: list[str] = list()
    list2: list[str] = list()
    for line in input:
        [numString1, numString2] = line.split("   ")
        list1.append(int(numString1))
        list2.append(int(numString2))
    return (list1, list2)


def getTotalDistance(input: list[str]) -> int:
    (list1, list2) = parseInput(input)
    list1.sort()
    list2.sort()
    distanceSum = 0
    for idx in range(len(list1)):
        distance = abs(list1[idx] - list2[idx])
        distanceSum += distance
    return distanceSum


def getSimilarity(input):
    (list1, list2) = parseInput(input)
    similaritySum = 0
    for idx in range(len(list1)):
        similarity = list2.count(list1[idx]) * list1[idx]
        similaritySum += similarity
    return similaritySum


if __name__ == "__main__":
    print(getTotalDistance(puzzleInput))
    print(getSimilarity(puzzleInput))
