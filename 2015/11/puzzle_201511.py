import re
from puzzle_201511_input import puzzleInput


def nextPassword(input: str):
    valid = False
    newPassword = input
    while not valid:
        newPassword = increment(newPassword)
        valid = (
            ruleNoForbiddenLetters(newPassword)
            and ruleAtLeastTwoDifferentPairs(newPassword)
            and ruleAtLeastThreeAscendingCharacters(newPassword)
        )
    return newPassword


def ruleAtLeastThreeAscendingCharacters(value: str) -> bool:
    count = 1
    previousChar = chr(0)
    passed = False
    for char in value:
        neededCharForSequence = chr(int.from_bytes(previousChar.encode()) + 1)
        if char == neededCharForSequence:
            count += 1
            passed = passed or count == 3
        else:
            count = 1
        previousChar = char
    return passed


def ruleNoForbiddenLetters(value: str) -> bool:
    forbiddenCharacters = value.count("i") + value.count("o") + value.count("l")
    return forbiddenCharacters == 0


def ruleAtLeastTwoDifferentPairs(value: str) -> bool:
    result = re.search(r"(?P<pair1>([a-z])\2).*(?P<pair2>([a-z])\4)", value)
    pair1 = None
    pair2 = None
    if result is not None:
        pair1 = result.group("pair1")
        pair2 = result.group("pair2")
    return pair1 != pair2


def increment(value: str) -> str:
    reversedValue = value[::-1]
    wrapAround = True
    result = ""
    if reversedValue[0] == "z":
        for char in reversedValue:
            charValue = int.from_bytes(char.encode()) - 97
            if wrapAround:
                charValue += 1
            wrapAround = charValue // 26 > 0
            charValue = charValue % 26 + 97
            result += chr(charValue)
        if wrapAround:
            result += "a"
    elif not ruleNoForbiddenLetters(value):
        regexResult = re.search(r"i|l|o", value)
        indexOfForbiddenCharacter = regexResult.regs[0][0]
        forbiddenCharacter = value[
            indexOfForbiddenCharacter : indexOfForbiddenCharacter + 1
        ]
        newChar = (
            forbiddenCharacter.replace("i", "j").replace("l", "m").replace("o", "p")
        )
        result = (
            value[0:indexOfForbiddenCharacter]
            + newChar
            + "a" * (len(value) - indexOfForbiddenCharacter - 1)
        )
        result = result[::-1]
    else:
        result = chr(int.from_bytes(reversedValue[0].encode()) + 1) + reversedValue[1::]
    return result[::-1]


if __name__ == "__main__":
    print(nextPassword(puzzleInput))
    print(nextPassword(nextPassword(puzzleInput)))
