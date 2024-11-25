from operator import attrgetter
import re
from puzzle_201514_input import puzzleInput


class Reindeer:
    name: str
    speedPerSecond: int
    flyDurationInSeconds: int
    restDurationInSeconds: int

    state: str
    timeRemainingInState: int
    distance: int
    score: int

    def __init__(
        self,
        name: str,
        speedPerSecond: int,
        flyDurationInSeconds: int,
        restDurationInSeconds: int,
    ) -> None:
        self.name = name
        self.speedPerSecond = speedPerSecond
        self.flyDurationInSeconds = flyDurationInSeconds
        self.restDurationInSeconds = restDurationInSeconds
        self.distance = 0
        self.score = 0
        self.state = "flying"
        self.timeRemainingInState = flyDurationInSeconds

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Reindeer):
            return False
        return (
            self.name == value.name
            and self.speedPerSecond == value.speedPerSecond
            and self.flyDurationInSeconds == value.flyDurationInSeconds
            and self.restDurationInSeconds == value.restDurationInSeconds
            and self.distance == value.distance
            and self.state == value.state
            and self.timeRemainingInState == value.timeRemainingInState
        )

    def run(self):
        if self.timeRemainingInState == 0:
            if self.state == "flying":
                self.state = "resting"
                self.timeRemainingInState = self.restDurationInSeconds
            elif self.state == "resting":
                self.state = "flying"
                self.timeRemainingInState = self.flyDurationInSeconds
        if self.state == "flying":
            self.distance += self.speedPerSecond
        self.timeRemainingInState -= 1


def firstRace(input: list[str], duration: int) -> Reindeer:
    reindeers = parseInput(input)
    for _ in range(duration):
        for reindeer in reindeers:
            reindeer.run()
    return max(reindeers, key=attrgetter("distance"))


def secondRace(input: list[str], duration: int) -> Reindeer:
    reindeers = parseInput(input)
    for _ in range(duration):
        for reindeer in reindeers:
            reindeer.run()
        highestDistance = max(reindeers, key=attrgetter("distance")).distance
        reindeersWithHighestDistance = [
            reindeer for reindeer in reindeers if reindeer.distance == highestDistance
        ]
        for reindeer in reindeersWithHighestDistance:
            reindeer.score += 1
    return max(reindeers, key=attrgetter("score"))


def parseInput(input: list[str]) -> list[Reindeer]:
    reindeers = list()
    for line in input:
        searchResult = re.search(
            r"(?P<name>\w+) can fly (?P<speed>\d+) km\/s for (?P<flyDuration>\d+) seconds, but then must rest for (?P<restDuration>\d+) seconds",
            line,
        )
        reindeer = Reindeer(
            searchResult.group("name"),
            int(searchResult.group("speed")),
            int(searchResult.group("flyDuration")),
            int(searchResult.group("restDuration")),
        )
        reindeers.append(reindeer)
    return reindeers


if __name__ == "__main__":
    print(firstRace(puzzleInput, 2503).distance)
    print(secondRace(puzzleInput, 2503).score)
