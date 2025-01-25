import pytest
from puzzle_201519 import do_puzzle_part1, do_puzzle_part2
from puzzle_201519_input import puzzleInput, replacement_list


@pytest.mark.parametrize(
    "replacement, input, output",
    [
        ([("H", "HO"), ("H", "OH"), ("O", "HH")], "HOH", 4),
        ([("H", "HO"), ("H", "OH"), ("O", "HH")], "HOHOHO", 7),
        (replacement_list, puzzleInput, 535),
    ],
)
def test_do_puzzle_part1(replacement, input, output):
    assert do_puzzle_part1(replacement, input) == output


@pytest.mark.parametrize(
    "replacement, molecule_to_generate, output",
    [
        ([("H", "HO"), ("H", "OH"), ("O", "HH"), ("e", "H"), ("e", "O")], "HOH", 3),
        ([("H", "HO"), ("H", "OH"), ("O", "HH"), ("e", "H"), ("e", "O")], "HOHOHO", 6),
        (replacement_list, puzzleInput, 212),
    ],
)
def test_do_puzzle_part2(replacement, molecule_to_generate, output):
    assert do_puzzle_part2(replacement, molecule_to_generate) == output
