from puzzle_201502_input import puzzleInput
from functools import reduce


def calculateTotalNeededWrappingPaper(input: list[str]):
    return reduce(
        lambda previous, input: previous + getNeededWrappingPaperForBox(input), input, 0
    )


def do_puzzle_part2(input):
    return None


def getNeededWrappingPaperForBox(input) -> int:
    dimensions = extractDimensionsAsInt(input)
    surfaceOfSmallestSide = getSurfaceOfSmallestSide(*dimensions)
    surfaceOfBox = calculateSurfaceOfBox(*dimensions)
    return surfaceOfBox + surfaceOfSmallestSide


def extractDimensionsAsInt(input: str) -> tuple[int, int, int]:
    return tuple(map(int, input.split("x")))


def getSurfaceOfSmallestSide(length: int, width: int, height: int) -> int:
    return min(length * width, width * height, height * length)


def calculateSurfaceOfBox(length: int, width: int, height: int) -> int:
    return 2 * length * width + 2 * width * height + 2 * height * length


print(calculateTotalNeededWrappingPaper(puzzleInput))
print(do_puzzle_part2(puzzleInput))
