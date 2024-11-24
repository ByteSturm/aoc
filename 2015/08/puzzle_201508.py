import re
from puzzle_201508_input import puzzleInput


def do_puzzle_part1(input: list[str]):
    codeLength = 0
    stringLength = 0
    for string in input:
        lengths = calculateLengths(string)
        codeLength += lengths["code"]
        stringLength += lengths["string"]
    return codeLength - stringLength


def do_puzzle_part2(input):
    codeLength = 0
    encodedLength = 0
    for string in input:
        lengths = calculateLengthOfencodedString(string)
        codeLength += lengths["code"]
        encodedLength += lengths["encoded"]
    return encodedLength - codeLength


def decodeAsciiChars(match: re.Match[str]):
    value = match.group("asciiValue")
    char = chr(int(value, 16))
    return char


def calculateLengths(input: str):
    codeLength = len(input)
    withoutQuotes = input.removeprefix('"').removesuffix('"')
    asciiReplaced = re.sub(
        r"\\x(?P<asciiValue>[a-f0-9]{2})",
        decodeAsciiChars,
        withoutQuotes,
    )
    noSingleBackslashes = re.sub(
        r"\\(?P<singlechar>[^\\])",
        lambda match: match.group("singlechar"),
        asciiReplaced,
    )
    reducedSlashes = noSingleBackslashes.replace("\\\\", "\\")
    stringLength = len(reducedSlashes)
    return {"code": codeLength, "string": stringLength}


def calculateLengthOfencodedString(input: str):
    codeLength = len(input)
    replacedDoubleQuotes = input.replace('"', '""')
    replacedBackslashes = replacedDoubleQuotes.replace("\\", "\\\\")
    wrappedInQuotes = '"' + replacedBackslashes + '"'
    encodedLength = len(wrappedInQuotes)
    return {"code": codeLength, "encoded": encodedLength}


if __name__ == "__main__":
    print(do_puzzle_part1(puzzleInput))
    print(do_puzzle_part2(puzzleInput))
