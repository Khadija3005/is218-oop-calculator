import math

from calculator import Add, Subtract, History


def get_number(prompt):
    value = float(input(prompt))

    if not math.isfinite(value):
        raise ValueError

    return value


def main():
    history = History()

    print("Calculator")
    print("Type 'help' to see available commands.")

    while True:
        try:
            command = input("> ").strip().lower()
        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break

        if command == "exit":
            print("Goodbye!")
            break

        elif command == "help":
            print("Available commands: add, subtract, history, remove, help, exit")

        elif command == "history":
            calculations = history.get_all()

            if not calculations:
                print("Calculation History")
                print("No calculations yet.")
            else:
                print("Calculation History")

                for index, calculation in enumerate(calculations, start=1):
                    name = calculation.__class__.__name__
                    result = calculation.calculate()

                    print(
                        f"{index}. {name}: "
                        f"{calculation.a:g}, {calculation.b:g} = {result:g}"
                    )

        elif command == "remove":
            calculations = history.get_all()

            if not calculations:
                print("No calculations to remove.")
            else:
                print("Calculation History")

                for index, calculation in enumerate(calculations, start=1):
                    name = calculation.__class__.__name__
                    result = calculation.calculate()

                    print(
                        f"{index}. {name}: "
                        f"{calculation.a:g}, {calculation.b:g} = {result:g}"
                    )

                try:
                    number = int(input("Enter calculation number to remove: "))

                    if number < 1 or number > len(calculations):
                        print("Invalid calculation number.")
                    else:
                        history.remove(number - 1)
                        print("Calculation removed.")

                except ValueError:
                    print("Invalid calculation number.")

        elif command == "add":
            try:
                first = get_number("First number: ")
                second = get_number("Second number: ")

                calculation = Add(first, second)
                history.add(calculation)

                print(f"Result: {calculation.calculate()}")

            except ValueError:
                print("Invalid number. Please enter numeric values.")

        elif command == "subtract":
            try:
                first = get_number("First number: ")
                second = get_number("Second number: ")

                calculation = Subtract(first, second)
                history.add(calculation)

                print(f"Result: {calculation.calculate()}")

            except ValueError:
                print("Invalid number. Please enter numeric values.")

        else:
            print("Unknown command. Type 'help' to see available commands.")


if __name__ == "__main__":  # pragma: no cover
    main()