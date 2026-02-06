from dataclasses import dataclass
from typing import Union
from calculator.exceptions import DivisionByZeroError


Number = Union[int, float]


@dataclass(frozen=True)
class Calculator:
    a: Number
    b: Number

    def add(self) -> Number:
        return self.a + self.b

    def subtract(self) -> Number:
        return self.a - self.b

    def multiply(self) -> Number:
        return self.a * self.b

    def divide(self) -> Number:
        if self.b == 0:
            raise DivisionByZeroError("Division by zero is not allowed.")
        return self.a / self.b
