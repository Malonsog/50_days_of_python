"""
Day 1: Division and Square-root

Write a function called divide_or_square that takes
one argument (a number), and returns the square root
of the number if it is divisible by 5, returns its
remainder if it is not divisible by 5.
For example, if you pass 10 as an argument, then your
function should return 3.16 as the square root.
"""

number = int(input("Enter a number: "))


def divide_or_square(number):
    if number % 5 == 0:
        return round(number ** 0.5, 2)
    else:
        return round(number % 5, 2)


print(divide_or_square(number))
