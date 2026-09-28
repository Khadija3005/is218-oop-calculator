from unittest.mock import patch

from calculator.__main__ import get_number, main


def test_exit(capsys):
    with patch("builtins.input", side_effect=["exit"]):
        main()

    output = capsys.readouterr().out
    assert "Calculator" in output
    assert "Goodbye!" in output


def test_help(capsys):
    with patch("builtins.input", side_effect=["help", "exit"]):
        main()

    output = capsys.readouterr().out
    assert "Available commands" in output
    assert "add" in output
    assert "subtract" in output


def test_unknown_command(capsys):
    with patch("builtins.input", side_effect=["pizza", "exit"]):
        main()

    output = capsys.readouterr().out
    assert "Unknown command" in output


def test_add_command(capsys):
    with patch(
        "builtins.input",
        side_effect=["add", "10", "5", "history", "exit"],
    ):
        main()

    output = capsys.readouterr().out
    assert "Result: 15.0" in output
    assert "1. Add: 10, 5 = 15" in output


def test_subtract_command(capsys):
    with patch(
        "builtins.input",
        side_effect=["subtract", "20", "7", "history", "exit"],
    ):
        main()

    output = capsys.readouterr().out
    assert "Result: 13.0" in output
    assert "1. Subtract: 20, 7 = 13" in output


def test_empty_history(capsys):
    with patch("builtins.input", side_effect=["history", "exit"]):
        main()

    output = capsys.readouterr().out
    assert "Calculation History" in output
    assert "No calculations yet." in output


def test_remove_command(capsys):
    with patch(
        "builtins.input",
        side_effect=[
            "add",
            "10",
            "5",
            "subtract",
            "20",
            "7",
            "remove",
            "1",
            "history",
            "exit",
        ],
    ):
        main()

    output = capsys.readouterr().out
    assert "Calculation removed." in output
    assert "1. Subtract: 20, 7 = 13" in output


def test_remove_empty_history(capsys):
    with patch("builtins.input", side_effect=["remove", "exit"]):
        main()

    output = capsys.readouterr().out
    assert "No calculations to remove." in output


def test_remove_invalid_number(capsys):
    with patch(
        "builtins.input",
        side_effect=["add", "10", "5", "remove", "99", "exit"],
    ):
        main()

    output = capsys.readouterr().out
    assert "Invalid calculation number." in output


def test_remove_invalid_text(capsys):
    with patch(
        "builtins.input",
        side_effect=["add", "10", "5", "remove", "hello", "exit"],
    ):
        main()

    output = capsys.readouterr().out
    assert "Invalid calculation number." in output


def test_add_invalid_number(capsys):
    with patch(
        "builtins.input",
        side_effect=["add", "hello", "history", "exit"],
    ):
        main()

    output = capsys.readouterr().out
    assert "Invalid number. Please enter numeric values." in output
    assert "No calculations yet." in output


def test_subtract_invalid_number(capsys):
    with patch(
        "builtins.input",
        side_effect=["subtract", "hello", "history", "exit"],
    ):
        main()

    output = capsys.readouterr().out
    assert "Invalid number. Please enter numeric values." in output
    assert "No calculations yet." in output


def test_nan_number():
    with patch("builtins.input", return_value="nan"):
        try:
            get_number("Number: ")
            assert False
        except ValueError:
            assert True


def test_infinite_number():
    with patch("builtins.input", return_value="inf"):
        try:
            get_number("Number: ")
            assert False
        except ValueError:
            assert True


def test_keyboard_interrupt(capsys):
    with patch("builtins.input", side_effect=KeyboardInterrupt):
        main()

    output = capsys.readouterr().out
    assert "Goodbye!" in output


def test_end_of_input(capsys):
    with patch("builtins.input", side_effect=EOFError):
        main()

    output = capsys.readouterr().out
    assert "Goodbye!" in output