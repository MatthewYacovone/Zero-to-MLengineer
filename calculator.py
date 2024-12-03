# Personalized Calculator
#
# Description: Build a command-line calculator that performs basic arithmetic operations (addition, subtraction, multiplication, division).
#              Extend it to include functionalities like percentage calculations or square roots.

# Goals: Learn Python syntax, input handling, and basic functions.
# Tools: None (pure Python).

import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is undefined."
    return a / b

def percent(val, percentage):
    return val * (percentage / 100)

def sqrt(val):
    if val < 0:
        return "Error: Square root of a negative number is undefined."
    return math.sqrt(val)

def calculator():
    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
        "percent": percent,
        "sqrt": sqrt
    }

    while True:
        operation = input("\nChoose an operation (add, subtract, multiply, divide, percent, sqrt) or 'exit' to quit. ")

        if operation == "exit":
            print("Goodbye!")
            break

        if operation not in operations:
            print("Invalid operation. Try again.")
            continue

        # Extended abilities
        try:
            if operation == "percent":
                percent_val = float(input("Enter the percentage: "))
                of_val = float(input("Enter the number: "))
                result = operations[operation](percent_val, of_val)
            elif operation == "sqrt":
                val = float(input("Enter a number: "))
                result = operations[operation](val)
            else:  # Basic abilities
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))
                result = operations[operation](num1, num2)

            print(f"Result: {result}")

        except ValueError:
            print("Invalid input. Please enter numeric values.")

calculator()

