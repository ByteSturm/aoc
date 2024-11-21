import hashlib
from puzzle_201504_input import puzzleInput


def getLowestNumber(input: str):
    idx = 0
    digestString = ""
    while not digestString.startswith("00000"):
        idx += 1
        stringToHash = f"{input}{idx}"
        digestString = hashlib.md5(stringToHash.encode()).hexdigest()
    return idx


def do_puzzle_part2(input: str):
    return None


print(getLowestNumber(puzzleInput))
print(do_puzzle_part2(puzzleInput))
