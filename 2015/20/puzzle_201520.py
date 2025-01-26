from math import isqrt
from puzzle_201520_input import puzzleInput


# This approach does not work out because a map with millions of entries is too slow.
# Here it's faster to get the divisors with a sieve approach, even if it means calculating
# some divisors multiple times.
def build_house_present_map(max_value: int) -> dict[int, list[int]]:
    factors: dict[int, int] = {house: 10 for house in range(1, max_value + 1)}
    print("Sum dict initialized")
    for elf in range(2, max_value + 1):
        for house in range(elf, max_value + 1, elf):
            factors[house] += elf * 10
        print(elf)
    return factors


def do_puzzle_part1_slowly(input: int) -> int:
    houses = build_house_present_map(input)
    houses_with_more_or_equal_presents = [
        house for house in houses if houses[house] >= input
    ]
    return min(houses_with_more_or_equal_presents)
    # This approach below is even slower becaue there I didn't save the sum in the map
    # instead I saved all divisors and afterwards calculated the sum.
    #
    # wanted_house = None
    # house_number = 1
    # while not wanted_house and house_number < input:
    #     presents_for_house = sum(factor * 10 for factor in houses[house_number])
    #     if presents_for_house >= input:
    #         wanted_house = house_number
    #     house_number += 1
    # return house_number


def get_divisors(value: int) -> set[int]:
    return sorted(
        {
            divisor
            for x in range(1, isqrt(value) + 1)
            if value % x == 0
            for divisor in (x, value // x)
        }
    )


def do_puzzle_part1(input: int) -> int:
    house_number = 0
    house_with_more_or_equal = None
    while not house_with_more_or_equal:
        house_number += 1
        divisors = get_divisors(house_number)
        presents = sum(divisors) * 10
        if presents >= input:
            house_with_more_or_equal = house_number
    return house_with_more_or_equal


def do_puzzle_part2(input):
    house_number = 0
    house_with_more_or_equal = None
    while not house_with_more_or_equal:
        house_number += 1
        divisors = get_divisors(house_number)
        relevant_divisors = [
            divisor for divisor in divisors if house_number // divisor <= 50
        ]
        presents = sum(relevant_divisors) * 11
        if presents >= input:
            house_with_more_or_equal = house_number
    return house_with_more_or_equal


if __name__ == "__main__":
    print(do_puzzle_part1(puzzleInput))
    print(do_puzzle_part2(puzzleInput))
