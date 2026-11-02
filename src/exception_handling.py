
# Python Exception Handling
# Demonstrating common errors using try-except

def divide_numbers():
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        result = num1 / num2
        print("Result:", result)

    except ValueError:
        print("Error: Please enter valid numbers.")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

    else:
        print("Division completed successfully.")

    finally:
        print("Program execution completed.")


def main():
    divide_numbers()


if __name__ == "__main__":
    main()
