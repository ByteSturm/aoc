import re
from typing import Callable
from puzzle_201505_input import puzzleInput


def isStringNice(input: str):
    numberOfVowels = len(re.findall(r"a|e|i|o|u", input))
    containsDuplicateCharacters = re.search(r"([a-z])\1", input) is not None
    containsBadSequence = re.search(r"ab|cd|pq|xy", input) is not None
    return (
        numberOfVowels >= 3 and containsDuplicateCharacters and not containsBadSequence
    )


def countNiceStrings(input: list[str], stringChecker: Callable[[str], bool]) -> int:
    return list(map(stringChecker, input)).count(True)


def isStringNiceV2(input: str) -> bool:
    containsDuplicateOfTwoCharacters = re.search(r"([a-z]{2}).*\1", input) is not None
    repetitionWithOneInBetween = re.search(r"([a-z])[a-z]\1", input) is not None
    return containsDuplicateOfTwoCharacters and repetitionWithOneInBetween


print(countNiceStrings(puzzleInput, isStringNice))
print(countNiceStrings(puzzleInput, isStringNiceV2))
