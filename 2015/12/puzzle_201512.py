from puzzle_201512_input import puzzleInput


def sumNumbersInComplexObject(input, ignoreRed=False, sum=0):
    intermediatSum = 0
    containsRed = False
    if type(input) is dict:
        for property in input.values():
            containsRed = containsRed or (ignoreRed and property == "red")
            intermediatSum += sumNumbersInComplexObject(property, ignoreRed, sum)
        if containsRed:
            intermediatSum = 0
    elif type(input) is list:
        for element in input:
            intermediatSum += sumNumbersInComplexObject(element, ignoreRed, sum)
    elif type(input) is int:
        intermediatSum = input
    return sum + intermediatSum


if __name__ == "__main__":
    print(sumNumbersInComplexObject(puzzleInput))
    print(sumNumbersInComplexObject(puzzleInput, True))
