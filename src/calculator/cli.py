from calculator.core import Calculator
from calculator.exceptions import DivisionByZeroError, InvalidInputError


MENU = """
Choose an operation:
1 - Addition
2 - Subtraction
3 - Multiplication
4 - Division
0 - Restart
Any other key - Exit
"""


def _read_number(prompt: str) -> float:
    try:
        return float(input(prompt))
    except ValueError:
        raise InvalidInputError("Input must be a valid number.")


def run() -> None:
    while True:
        try:
            a = _read_number("Enter a: ")
            b = _read_number("Enter b: ")

            calc = Calculator(a, b)

            print(MENU)
            choice = input("Your choice: ").strip()

            if choice == "1":
                print(calc.add())
            elif choice == "2":
                print(calc.subtract())
            elif choice == "3":
                print(calc.multiply())
            elif choice == "4":
                print(calc.divide())
            elif choice == "0":
                continue
            else:
                break

        except (DivisionByZeroError, InvalidInputError) as e:
            print(f"Error: {e}")
        except KeyboardInterrupt:
            break


if __name__ == "__main__":
    run()
