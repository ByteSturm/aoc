import pytest
from puzzle_201515 import (
    findBestMixture,
    findBestMixtureWithGivenCalories,
    Ingredient,
    nextValues,
    parseInput,
    calculateScore,
)
from puzzle_201515_input import puzzleInput


@pytest.mark.parametrize(
    "input, output",
    [
        (
            "Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8",
            Ingredient("Butterscotch", -1, -2, 6, 3, 8),
        ),
        (
            "Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3",
            Ingredient("Cinnamon", 2, 3, -2, -1, 3),
        ),
    ],
)
def test_parseInput(input, output):
    assert parseInput(input) == output


@pytest.mark.parametrize(
    "input, output",
    [
        (
            [
                (Ingredient("Butterscotch", -1, -2, 6, 3, 8), 75),
                (Ingredient("Cinnamon", 2, 3, -2, -1, 3), 25),
            ],
            0,
        ),
        (
            [
                (Ingredient("Butterscotch", -1, -2, 6, 3, 8), 44),
                (Ingredient("Cinnamon", 2, 3, -2, -1, 3), 56),
            ],
            62842880,
        ),
    ],
)
def test_calculateScore(input, output):
    assert calculateScore(input) == output


@pytest.mark.parametrize(
    "input, min, max, output",
    [
        ([1], 1, 100, [2]),
        ([1, 1], 1, 100, [2, 1]),
        ([99, 1], 1, 100, [1, 2]),
        ([99, 6], 5, 100, [5, 7]),
        ([2, 99, 99, 1], 1, 100, [3, 99, 99, 1]),
        ([99, 99, 99, 1], 1, 100, [1, 1, 1, 2]),
        ([99, 99, 99, 99], 1, 100, [1, 1, 1, 1]),
    ],
)
def test_nextValues(input, min, max, output):
    assert nextValues(input, min, max) == output


@pytest.mark.parametrize(
    "input, output",
    [
        (
            [
                "Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8",
                "Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3",
            ],
            62842880,
        ),
        (puzzleInput, 21367368),
    ],
)
def test_findBestMixture(input, output):
    assert findBestMixture(input) == output


@pytest.mark.parametrize(
    "input, output",
    [
        (
            [
                "Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8",
                "Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3",
            ],
            57600000,
        ),
        (puzzleInput, 1766400),
    ],
)
def test_findBestMixtureWithGivenCalories(input, output):
    assert findBestMixtureWithGivenCalories(input, 500) == output
