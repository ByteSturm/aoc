import pytest
from puzzle_201509 import (
    findShortestPathPermutation,
    findLongestPathPermutation,
)
from puzzle_201509_input import puzzleInput


@pytest.mark.parametrize(
    "graph, output",
    [
        ({}, 0),
        (
            ["London to Dublin = 464"],
            464,
        ),
        (
            [
                "London to Dublin = 464",
                "London to Belfast = 518",
                "Dublin to Belfast = 141",
                "Belfast to Dublin = 141",
            ],
            605,
        ),
        (puzzleInput, 251),
    ],
)
def test_findShortestPathPermutation(graph, output):
    assert findShortestPathPermutation(graph) == output


@pytest.mark.parametrize(
    "graph, output",
    [
        (
            [
                "London to Dublin = 464",
                "London to Belfast = 518",
                "Dublin to Belfast = 141",
                "Belfast to Dublin = 141",
            ],
            982,
        ),
        (puzzleInput, 898),
    ],
)
def test_findLongestPathPermutation(graph, output):
    assert findLongestPathPermutation(graph) == output
