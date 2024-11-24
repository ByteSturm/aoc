import re
from puzzle_201508_input import puzzleInput


def do_puzzle_part1(input: list[str]):
    codeLength = 0
    stringLength = 0
    for string in input:
        lengths = calculateLengthsByCounting(string)
        codeLength += lengths["code"]
        stringLength += lengths["string"]
    return codeLength - stringLength


def do_puzzle_part2(input):
    codeLength = 0
    encodedLength = 0
    for string in input:
        lengths = calculateLengthOfencodedStringByCounting(string)
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


def calculateLengthsByCounting(input: str):
    codeLength = len(input)
    idx = 0
    stringLength = -2
    while idx < codeLength:
        stringLength += 1
        step = 1
        if input[idx] == "\\":
            if input[idx + 1] == "\\" or input[idx + 1] == '"':
                step = 2
            elif input[idx + 1] == "x":
                step = 4
        idx += step
    return {"code": codeLength, "string": stringLength}


def calculateLengthOfencodedStringByCounting(input: str):
    codeLength = len(input)
    encodedLength = 2
    for char in input:
        if char == "\\" or char == '"':
            encodedLength += 2
        else:
            encodedLength += 1
    return {"code": codeLength, "encoded": encodedLength}


if __name__ == "__main__":
    print(do_puzzle_part1(puzzleInput))
    print(do_puzzle_part2(puzzleInput))
