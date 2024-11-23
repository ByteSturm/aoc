import re
from enum import Enum
from typing import Self, Union
from dataclasses import dataclass
from puzzle_201507_input import puzzleInput
from puzzle_201507_input2 import puzzleInput2


class Operation(Enum):
    AND = "AND"
    OR = "OR"
    NOT = "NOT"
    LSHIFT = "LSHFIT"
    RSHIFT = "RSHIFT"


class Wire:
    identifier: str
    input: int | Self | "Gate" | None

    def __init__(self, identifier: str, input: int | Self | "Gate" | None = None):
        self.identifier = identifier
        self.input = input

    def signal(self) -> int:
        if isinstance(self.input, Gate):
            return self.input.output()
        elif isinstance(self.input, Wire):
            return self.input.signal()
        else:
            return self.input

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Wire):
            return False
        return self.identifier == value.identifier and self.input == value.input


class Gate:
    operation: Operation
    input1: Wire
    input2: Union[Wire, int, None] = None
    result: int | None

    def __init__(
        self,
        operation: Operation,
        input1: Union["Wire", int],
        input2: Union["Wire", int, None] = None,
    ):
        self.input1 = input1
        self.input2 = input2
        self.operation = operation
        self.result = None

    def output(self) -> int:
        if self.result is not None:
            return self.result

        if isinstance(self.input1, Wire):
            value1 = self.input1.signal()
        else:
            value1 = self.input1
        if isinstance(self.input2, Wire):
            value2 = self.input2.signal()
        else:
            value2 = self.input2

        if self.operation == Operation.AND:
            self.result = value1 & value2
        elif self.operation == Operation.OR:
            self.result = value1 | value2
        elif self.operation == Operation.NOT:
            self.result = ~value1 & 0xFFFF
        elif self.operation == Operation.RSHIFT:
            self.result = value1 >> value2
        elif self.operation == Operation.LSHIFT:
            self.result = value1 << value2
        else:
            self.result = value1

        return self.result

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Gate):
            return False
        return (
            self.operation == value.operation
            and self.input1 == value.input1
            and self.input2 == value.input2
        )


@dataclass
class ParsedInput:
    outputName: str
    inputNameOrValue1: str | None = None
    operationName: Operation | None = None
    inputNameOrValue2: str | None = None


class Circuit:
    circuit: dict[str, Wire] = dict()

    def parseLine(input: str) -> ParsedInput:
        input1Regex = r"(?P<input1>[a-z0-9]+)?"
        input2Regex = r"(?P<input2>[a-z0-9]+)?"
        operationRegex = r"(?P<operation>AND|OR|RSHIFT|LSHIFT|NOT)?"
        outputRegex = r"(?P<output>[a-z]+)"
        captureGroups = re.search(
            input1Regex
            + " ?"
            + operationRegex
            + " ?"
            + input2Regex
            + " -> "
            + outputRegex,
            input,
        )

        operationEnum = None
        if captureGroups.groupdict()["operation"] is not None:
            operationEnum = Operation[captureGroups.groupdict()["operation"]]

        return ParsedInput(
            captureGroups.groupdict()["output"],
            captureGroups.groupdict()["input1"],
            operationEnum,
            captureGroups.groupdict()["input2"],
        )

    def createCircuit(input: list[str]) -> Self:
        instance = Circuit()
        for line in input:
            parsedLine = Circuit.parseLine(line)
            outputWire = instance.setWire(parsedLine.outputName)

            if parsedLine.operationName is not None:
                outputWire.input = instance.connectNewGate(parsedLine)
            elif parsedLine.inputNameOrValue1.isdigit():
                outputWire.input = int(parsedLine.inputNameOrValue1)
            else:
                outputWire.input = instance.setWire(parsedLine.inputNameOrValue1)

            instance.circuit[parsedLine.outputName] = outputWire
        return instance

    def setWire(self, name: str) -> Wire:
        return self.circuit.setdefault(name, Wire(name))

    def connectNewGate(self, parsedLine: ParsedInput) -> Gate:
        newGate: Gate = None

        if parsedLine.inputNameOrValue1 is not None:
            if parsedLine.inputNameOrValue1.isdigit():
                input1 = int(parsedLine.inputNameOrValue1)
            else:
                input1 = self.setWire(parsedLine.inputNameOrValue1)
        if parsedLine.inputNameOrValue2 is not None:
            if parsedLine.inputNameOrValue2.isdigit():
                input2 = int(parsedLine.inputNameOrValue2)
            else:
                input2 = self.setWire(parsedLine.inputNameOrValue2)

        if parsedLine.operationName == Operation.NOT:
            newGate = Gate(parsedLine.operationName, input2)
        else:
            newGate = Gate(parsedLine.operationName, input1, input2)

        return newGate

    def executeCircuit(self) -> dict[str, int]:
        result: dict[str, int] = dict()
        for wire in self.circuit.values():
            result[wire.identifier] = wire.signal()
        return result


if __name__ == "__main__":
    print(Circuit.createCircuit(puzzleInput).circuit["a"].signal())
    print(Circuit.createCircuit(puzzleInput2).circuit["a"].signal())
