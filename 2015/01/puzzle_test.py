import pytest
from puzzle import getFloor

@pytest.mark.parametrize("input, output", [
    ("(())",0), ("()()",0),
    ("(((",3), ("(()(()(",3), ("))(((((",3),
    ("())",-1), ("))(",-1),
    (")))",-3), (")())())",-3)
])
def test_getFloor(input, output):
    assert getFloor(input) == output
