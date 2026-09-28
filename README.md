# OOP Calculator

This project is a command-line calculator created with Python. It uses object-oriented programming concepts and allows users to perform calculations and manage calculation history.

## Features

The calculator supports these commands:

- `add` - Add two numbers
- `subtract` - Subtract two numbers
- `history` - View calculation history
- `remove` - Remove a calculation from history
- `help` - Show available commands
- `exit` - Close the calculator

The calculator also handles invalid input, `nan`, `inf`, Ctrl+C, and end-of-input without crashing.

## Installation

Clone the repository:

```bash
git clone git@github.com:Khadija3005/is218-oop-calculator.git
cd is218-oop-calculator
```

Create and activate a virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
```

Install the required packages:

```bash
python -m pip install -r requirements.txt
```

## Running the Calculator

Run the calculator with:

```bash
python -m calculator
```

Type `help` to see the available commands.

## Running Tests

Run the tests with:

```bash
python -m pytest
```

The project uses pytest and pytest-cov. The tests require 100% line and branch coverage.

## Design

This project uses object-oriented programming. The `Calculation` class is an abstract base class. The `Add` and `Subtract` classes inherit from it and perform their own calculations.

The `History` class stores completed calculations. It allows calculations to be added, viewed, removed, and cleared.

Keeping the calculations, history, and command-line interface separate makes the program easier to understand, test, and update.

## Continuous Integration

GitHub Actions automatically runs the tests when code is pushed or a pull request is created. The workflow tests the project using Python 3.11, 3.12, 3.13, and 3.14.