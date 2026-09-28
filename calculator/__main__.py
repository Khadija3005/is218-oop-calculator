from calculator import Add, Subtract, History


def main():
    history = History()

    print("Calculator")
    print("Type 'help' to see available commands.")

    while True:
        command = input("> ").strip().lower()

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

                number = int(input("Enter calculation number to remove: "))
                history.remove(number - 1)

                print("Calculation removed.")

        elif command == "add":
            first = float(input("First number: "))
            second = float(input("Second number: "))

            calculation = Add(first, second)
            history.add(calculation)

            print(f"Result: {calculation.calculate()}")

        elif command == "subtract":
            first = float(input("First number: "))
            second = float(input("Second number: "))

            calculation = Subtract(first, second)
            history.add(calculation)

            print(f"Result: {calculation.calculate()}")
        else:
            print("Unknown command. Type 'help' to see available commands.")


if __name__ == "__main__":
    main()