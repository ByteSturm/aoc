import re
from dataclasses import dataclass
from puzzle_201515_input import puzzleInput


@dataclass
class Ingredient:
    name: str
    capacity: int
    durability: int
    flavor: int
    texture: int
    calories: int


def parseInput(line: str) -> Ingredient:
    searchResult = re.search(
        r"(?P<name>\w+): capacity (?P<capacity>-?\d+), durability (?P<durability>-?\d+), flavor (?P<flavor>-?\d+), texture (?P<texture>-?\d+), calories (?P<calories>-?\d+)",
        line,
    )
    return Ingredient(
        searchResult.group("name"),
        int(searchResult.group("capacity")),
        int(searchResult.group("durability")),
        int(searchResult.group("flavor")),
        int(searchResult.group("texture")),
        int(searchResult.group("calories")),
    )


def calculateScore(ingredients: list[tuple[Ingredient, int]]) -> int:
    capacityScore = 0
    durabilityScore = 0
    flavorScore = 0
    textureScore = 0
    for ingredient, quantity in ingredients:
        capacityScore += ingredient.capacity * quantity
        durabilityScore += ingredient.durability * quantity
        flavorScore += ingredient.flavor * quantity
        textureScore += ingredient.texture * quantity
    return (
        max(capacityScore, 0)
        * max(durabilityScore, 0)
        * max(flavorScore, 0)
        * max(textureScore, 0)
    )


def calculateCalories(ingredients: list[tuple[Ingredient, int]]) -> int:
    caloriesPerIngredient = map(lambda tuple: tuple[0].calories * tuple[1], ingredients)
    return sum(caloriesPerIngredient)


def nextValues(values: list[int], minValue: int = 1, maxValue: int = 100) -> list[int]:
    overflow = 1
    for idx in range(0, len(values), 1):
        newValue = values[idx] + overflow
        overflow = newValue // maxValue
        values[idx] = (newValue % maxValue) + minValue * overflow
    return values


def findBestMixture(input: list[str]):
    ingredients = list(map(parseInput, input))
    ingredientAmounts = [1] * (len(ingredients) - 1)
    highscore = 0

    while ingredientAmounts[-1] < 99:
        lastIngredientAmount = 100 - sum(ingredientAmounts)
        ingredientsWithAmounts = list(
            zip(ingredients, ingredientAmounts + [lastIngredientAmount])
        )

        score = calculateScore(ingredientsWithAmounts)
        highscore = max(highscore, score)

        nextValues(ingredientAmounts)
    return highscore


def findBestMixtureWithGivenCalories(input: list[str], wantedCalories: int):
    ingredients = list(map(parseInput, input))
    ingredientAmounts = [1] * (len(ingredients) - 1)
    highscore = 0

    while ingredientAmounts[-1] < 99:
        lastIngredientAmount = 100 - sum(ingredientAmounts)
        ingredientsWithAmounts = list(
            zip(ingredients, ingredientAmounts + [lastIngredientAmount])
        )

        score = calculateScore(ingredientsWithAmounts)
        calories = calculateCalories(ingredientsWithAmounts)
        highscore = max(highscore, 0 if calories != wantedCalories else score)

        nextValues(ingredientAmounts)
    return highscore


if __name__ == "__main__":
    print(findBestMixture(puzzleInput))
    print(findBestMixtureWithGivenCalories(puzzleInput, 500))
