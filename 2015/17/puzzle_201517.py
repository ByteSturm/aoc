from puzzle_201517_input import puzzleInput


def subsets(numbers):
    if numbers == []:
        return [[]]
    x = subsets(numbers[1:])
    return x + [[numbers[0]] + y for y in x]


def do_puzzle_part1(liters: int, buckets: list[int]) -> int:
    return len(
        [combination for combination in subsets(buckets) if sum(combination) == liters]
    )


def do_puzzle_part2(liters: int, buckets: list[int]) -> int:
    validCombinations = [
        combination for combination in subsets(buckets) if sum(combination) == liters
    ]
    minLength = min(map(lambda x: len(x), validCombinations))
    smallestCombinations = list(
        filter(lambda x: len(x) == minLength, validCombinations)
    )
    return len(smallestCombinations)


if __name__ == "__main__":
    print(do_puzzle_part1(150, puzzleInput))
    print(do_puzzle_part2(150, puzzleInput))
