import pytest
from tests.hello import greet

def test_greeting():
    test_argument = "Monte Carlo"
    expected = "Hello Monte Carlo"
    actual = greet(test_argument)
    assert actual == expected, "Expected \"{0}\", but actual is \"{1}\"".format(expected, actual)
