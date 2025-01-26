import time
import pytest
from puzzle_201520 import (
    # build_house_present_map,
    do_puzzle_part1,
    do_puzzle_part2,
)
from puzzle_201520_input import puzzleInput


# @pytest.mark.parametrize(
#     "input, output",
#     [
#         (1, 10),
#         (2, 30),
#         (3, 40),
#         (4, 70),
#         (5, 60),
#         (6, 120),
#         (7, 80),
#         (8, 150),
#         (9, 130),
#         (puzzleInput, None),  # 831600
#     ],
# )
# def test_sum_with(input, output):
#     factors = build_house_present_map(input)
#     assert sum_with(factors[input], lambda x: x * 10) == output


@pytest.mark.parametrize(
    "input, output",
    [(130, 8), (666, 30), (123456, 3600), (7654321, 191520), (puzzleInput, 831600)],
)
def test_do_puzzle_part1(input, output):
    assert do_puzzle_part1(input) == output


@pytest.mark.parametrize("input, output", [(puzzleInput, 884520)])
def test_do_puzzle_part2(input, output):
    assert do_puzzle_part2(input) == output
