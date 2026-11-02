
# Python Debugging Example
# Find and fix errors in a program

# Original code with an error:
# The condition uses assignment (=) instead of comparison (==).

def calculate_average(marks):
    total = sum(marks)
    average = total / len(marks)
    return average


def main():
    marks = [80, 90, 70]

    try:
        average = calculate_average(marks)
        print("Average:", average)

        if average >= 40:
            print("Result: Pass")
        else:
            print("Result: Fail")

    except ZeroDivisionError:
        print("Error: No marks available.")

    except TypeError:
        print("Error: Invalid marks data.")


if __name__ == "__main__":
    main()
