import pytest
from puzzle_201514 import firstRace, secondRace, parseInput, Reindeer
from puzzle_201514_input import puzzleInput


@pytest.mark.parametrize(
    "input, output",
    [
        (
            [
                "Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds."
            ],
            [Reindeer("Comet", 14, 10, 127)],
        ),
        (
            [
                "Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."
            ],
            [Reindeer("Dancer", 16, 11, 162)],
        ),
    ],
)
def test_parseInput(input, output):
    assert parseInput(input) == output


@pytest.mark.parametrize(
    "reindeer, duration, output",
    [
        (Reindeer("Comet", 14, 10, 127), 10, 140),
        (Reindeer("Dancer", 16, 11, 162), 10, 160),
        (Reindeer("Comet", 14, 10, 127), 11, 140),
        (Reindeer("Dancer", 16, 11, 162), 11, 176),
        (Reindeer("Dancer", 16, 11, 162), 12, 176),
        (Reindeer("Comet", 14, 10, 127), 137, 140),
        (Reindeer("Dancer", 16, 11, 162), 173, 176),
        (Reindeer("Comet", 14, 10, 127), 138, 154),
        (Reindeer("Dancer", 16, 11, 162), 174, 192),
        (Reindeer("Comet", 14, 10, 127), 1000, 1120),
        (Reindeer("Dancer", 16, 11, 162), 1000, 1056),
    ],
)
def test_reindeers(reindeer, duration, output):
    for _ in range(duration):
        reindeer.run()
    assert reindeer.distance == output


@pytest.mark.parametrize(
    "input, duration, winnerName, winnerDistance",
    [
        (
            [
                "Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.",
                "Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.",
            ],
            1000,
            "Comet",
            1120,
        ),
        (puzzleInput, 2503, "Donner", 2655),
    ],
)
def test_firstRace(input, duration, winnerName, winnerDistance):
    winner = firstRace(input, duration)
    assert winner.name == winnerName
    assert winner.distance == winnerDistance


@pytest.mark.parametrize(
    "input, duration, winnerName, winnerScore",
    [
        (
            [
                "Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.",
                "Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.",
            ],
            1,
            "Dancer",
            1,
        ),
        (
            [
                "Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.",
                "Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.",
            ],
            140,
            "Dancer",
            139,
        ),
        (
            [
                "Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.",
                "Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds.",
            ],
            1000,
            "Dancer",
            689,
        ),
        (puzzleInput, 2503, "Vixen", 1059),
    ],
)
def test_secondRace(input, duration, winnerName, winnerScore):
    winner = secondRace(input, duration)
    assert winner.name == winnerName
    assert winner.score == winnerScore
