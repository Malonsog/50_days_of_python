"""
Day 23: Simple Calculator
Create a simple calculator.
The calculator should be able to perform basic math operations, add, subtract, divide and multiply.
The calculator should take input from users.
The calculator should be able to handle ZeroDivisionError, NameError, and ValueError.
"""


def simple_calc() -> str:
    result = 0.0
    print(f"Operations to perform:")
    print(f"a) Addition: a + b")
    print(f"b) Subtraction: a - b")
    print(f"c) Multiplication: a * b")
    print(f"d) Division: a / b")
    while True:
        try:
            operation = input("Please select the letter of the operation you want to perform: ")
            if operation.lower() not in ("a", "b", "c", "d"):
                raise ValueError(f"Invalid input.")
            else:
                break
        except ValueError as e:
            print(f"{e} Please select a valid operation.")
    while True:
        try:
            a = float(input("Input the first number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    while True:
        try:
            b = float(input("Input the second number: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    if operation.lower() == "a":
        result = a + b
    elif operation.lower() == "b":
        result = a - b
    elif operation.lower() == "c":
        result = a * b
    elif operation.lower() == "d":
        if b == 0:
            return f"Error: Cannot divide by zero. Please try again."
        result = a / b
    return f"The result of your operation is: {result: .1f}"


# Version from the book (I liked mine better):
import operator


def calculator():
    try:
        num1 = int(input("Enter number: "))
        # asking the user to pick an operator
        opt = input("Pick operator(+,-,*,/) : ")
        num2 = int(input('Enter another number: '))
        if opt not in ['+', '-', '*', '/'] or len(opt) > 1:
            print('Please enter a valid operator')
    except ValueError:
        print('Please enter a valid number')
    except ZeroDivisionError:
        print('You cannot divide a number by zero.Try again')
    else:
        if opt == '+':
            return f'ans is: {operator.add(num1, num2)}'
        elif opt == '-':
            return f'ans is: {operator.sub(num1, num2)}'
        elif opt == '*':
            return f'ans is: {operator.mul(num1, num2)}'
        elif opt == '/':
            return f' ans is: {operator.truediv(num1, num2)}'
    return 'Try again'


print(simple_calc())
