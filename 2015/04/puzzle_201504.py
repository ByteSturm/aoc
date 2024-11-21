import hashlib
from puzzle_201504_input import puzzleInput


def getLowestNumberForHashWithFiveZeroes(input: str):
    return getLowestNumberForHashStartingWith(input, "00000")


def getLowestNumberForHashWithSixZeroes(input: str):
    return getLowestNumberForHashStartingWith(input, "000000")


def getLowestNumberForHashStartingWith(input: str, startCriteria: str):
    idx = 0
    digestString = ""
    while not digestString.startswith(startCriteria):
        idx += 1
        stringToHash = f"{input}{idx}"
        digestString = hashlib.md5(stringToHash.encode()).hexdigest()
    return idx


print(getLowestNumberForHashWithFiveZeroes(puzzleInput))
print(getLowestNumberForHashWithSixZeroes(puzzleInput))
