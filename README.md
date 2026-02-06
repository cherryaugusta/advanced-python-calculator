# Advanced Python Calculator

## Overview

This project is a professional, command-line based calculator designed to demonstrate advanced Python programming practices, clean software architecture, and strong GitHub repository standards. It significantly improves upon basic procedural calculator examples by applying object-oriented design, immutability, exception handling, testing, and modular structure.

## Features

- Immutable calculator core using `@dataclass`
- Strong input validation and custom exceptions
- Clean separation of business logic and CLI interface
- Fully testable design with pytest
- Python type hints for clarity and correctness
- Production-ready repository structure

## Project Structure

advanced-python-calculator/
├── src/calculator # Application source code
├── tests # Unit tests
├── README.md
├── LICENSE
└── pyproject.toml

## Installation

```bash
git clone https://github.com/your-username/advanced-python-calculator.git
cd advanced-python-calculator
python -m venv .venv
source .venv/bin/activate
pip install -e .
```

## Running the Application

python -m calculator.cli

## Example Usage

Enter a: 10
Enter b: 5

1 - Addition
2 - Subtraction
3 - Multiplication
4 - Division
0 - Restart
Any other key - Exit

Your choice: 4
Result: 2.0

## Running Tests

pytest

## Design Principles Demonstrated

• Single Responsibility Principle
• Immutability
• Explicit error handling
• Test-driven mindset
• Clean CLI interfaces
• Readable, maintainable code

## Disclaimer

This project is created strictly for educational purposes and portfolio demonstration only. It is not intended for production financial calculations or mission-critical systems.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
