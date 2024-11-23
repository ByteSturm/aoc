from puzzle_201502_input import puzzleInput
from functools import reduce


def calculateTotalNeededWrappingPaper(input: list[str]):
    return reduce(
        lambda previous, input: previous + getNeededWrappingPaperForBox(input), input, 0
    )


def calculateTotalRibbonNeeded(input: list[str]):
    return reduce(
        lambda previous, input: previous + getNeededRibbonForBox(input), input, 0
    )


def getNeededWrappingPaperForBox(input: str) -> int:
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


def getNeededRibbonForBox(input: str) -> int:
    dimensions = extractDimensionsAsInt(input)
    ribbonToWrapAround = getSmallestPerimeter(*dimensions)
    ribbonForBow = calculateRibbonNeededForBow(*dimensions)
    return ribbonToWrapAround + ribbonForBow


def getSmallestPerimeter(length: int, width: int, height: int) -> int:
    return min(2 * (length + width), 2 * (width + height), 2 * (height + length))


def calculateRibbonNeededForBow(length: int, width: int, height: int) -> int:
    return length * width * height


if __name__ == "__main__":
    print(calculateTotalNeededWrappingPaper(puzzleInput))
    print(calculateTotalRibbonNeeded(puzzleInput))
