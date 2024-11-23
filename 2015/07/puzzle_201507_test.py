import pytest
from puzzle_201507 import (
    Operation,
    Gate,
    Wire,
    Circuit,
    ParsedInput,
)


@pytest.mark.parametrize(
    "input, output",
    [
        (
            [
                "NOT x -> h",
                "NOT y -> i",
                "123 -> x",
                "456 -> y",
                "x AND y -> d",
                "x OR y -> e",
                "x LSHIFT 2 -> f",
                "y RSHIFT 2 -> g",
            ],
            {
                "d": 72,
                "e": 507,
                "f": 492,
                "g": 114,
                "h": 65412,
                "i": 65079,
                "x": 123,
                "y": 456,
            },
        )
    ],
)
def test_executeCircuit(input, output):
    createdCircuit = Circuit.createCircuit(input)
    result = createdCircuit.executeCircuit()
    assert result == output


def test_simpleWire():
    simpleWire = Wire("simpleWire", 2)
    assert simpleWire.identifier == "simpleWire"
    assert simpleWire.signal() == 2


def test_wireToWire():
    inputWire = Wire("simpleWire", 5)
    wireToWire = Wire("wireToWire", inputWire)
    assert wireToWire.identifier == "wireToWire"
    assert wireToWire.signal() == 5


def test_andGate():
    inputWire1 = Wire("inputWire", 3)
    inputWire2 = Wire("inputWire", 5)
    gate = Gate(Operation.AND, inputWire1, inputWire2)
    assert gate.output() == 1


def test_orGate():
    inputWire1 = Wire("inputWire", 3)
    inputWire2 = Wire("inputWire", 4)
    gate = Gate(Operation.OR, inputWire1, inputWire2)
    assert gate.output() == 7


def test_notGate():
    inputWire = Wire("inputWire", 3)
    gate = Gate(Operation.NOT, inputWire)
    assert gate.output() == 65532


def test_rightShiftGate():
    inputWire = Wire("inputWire", 3)
    gate = Gate(Operation.RSHIFT, inputWire, 2)
    assert gate.output() == 0


def test_leftShiftGate():
    inputWire = Wire("inputWire", 3)
    gate = Gate(Operation.LSHIFT, inputWire, 2)
    assert gate.output() == 12


@pytest.mark.parametrize(
    "input, output",
    [
        ("123 -> x", ParsedInput("x", inputNameOrValue1="123")),
        ("456 -> y", ParsedInput("y", inputNameOrValue1="456")),
        ("x AND y -> d", ParsedInput("d", "x", Operation.AND, "y")),
        ("x OR y -> e", ParsedInput("e", "x", Operation.OR, "y")),
        ("x LSHIFT 2 -> f", ParsedInput("f", "x", Operation.LSHIFT, "2")),
        ("y RSHIFT 2 -> g", ParsedInput("g", "y", Operation.RSHIFT, "2")),
        ("NOT x -> h", ParsedInput("h", None, Operation.NOT, "x")),
        ("NOT y -> i", ParsedInput("i", None, Operation.NOT, "y")),
    ],
)
def test_parseLine(input, output):
    assert Circuit.parseLine(input) == output


def test_createCircuit():
    input = [
        "NOT x -> h",
        "NOT y -> i",
        "123 -> x",
        "456 -> y",
        "x AND y -> d",
        "x OR y -> e",
        "x LSHIFT 2 -> f",
        "y RSHIFT 2 -> g",
    ]
    circuit = Circuit.createCircuit(input)

    xWire = Wire("x", 123)
    yWire = Wire("y", 456)
    dWire = Wire("d", Gate(Operation.AND, xWire, yWire))
    eWire = Wire("e", Gate(Operation.OR, xWire, yWire))
    fWire = Wire("f", Gate(Operation.LSHIFT, xWire, 2))
    gWire = Wire("g", Gate(Operation.RSHIFT, xWire, 2))
    hWire = Wire("h", Gate(Operation.NOT, xWire))
    iWire = Wire("i", Gate(Operation.NOT, yWire))
    expectedCircuit = Circuit()
    expectedCircuit.circuit["x"] = xWire
    expectedCircuit.circuit["y"] = yWire
    expectedCircuit.circuit["d"] = dWire
    expectedCircuit.circuit["e"] = eWire
    expectedCircuit.circuit["f"] = fWire
    expectedCircuit.circuit["g"] = gWire
    expectedCircuit.circuit["h"] = hWire
    expectedCircuit.circuit["i"] = iWire

    assert circuit.circuit == expectedCircuit.circuit
