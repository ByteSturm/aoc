from puzzle_201510_input import puzzleInput


def do_puzzle_part1(input):
    currentString = input
    for _ in range(40):
        currentString = lookAndSay(currentString)

    return len(currentString)


def do_puzzle_part2(input):
    currentString = input
    for _ in range(50):
        currentString = lookAndSay(currentString)

    return len(currentString)


def lookAndSay(input: str) -> str:
    count = 0
    currentChar = input[0]
    result = ""
    for inputChar in input:
        if inputChar == currentChar:
            count += 1
        else:
            result += str(count) + currentChar
            count = 1
            currentChar = inputChar
    result += str(count) + currentChar
    return result


if __name__ == "__main__":
    print(do_puzzle_part1(puzzleInput))
    print(do_puzzle_part2(puzzleInput))
