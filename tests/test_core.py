import pytest
from calculator.core import Calculator
from calculator.exceptions import DivisionByZeroError


def test_add():
    assert Calculator(2, 3).add() == 5


def test_subtract():
    assert Calculator(5, 3).subtract() == 2


def test_multiply():
    assert Calculator(4, 2).multiply() == 8


def test_divide():
    assert Calculator(10, 2).divide() == 5


def test_divide_by_zero():
    with pytest.raises(DivisionByZeroError):
        Calculator(10, 0).divide()
