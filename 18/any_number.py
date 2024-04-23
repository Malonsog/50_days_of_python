"""
Day 18: Any Number of Arguments
Write a function called any_number that can receive any number of arguments(integers and floats)
and return the average of those integers.
If you pass 12, 90, 12, 34 as arguments your function should return 37.0 as average.
If you pass 12, 90 your function should return 51.0 as average.
"""


def any_number(*numbers):
    total_sum = 0
    for number in numbers:
        if isinstance(number, (int, float)):
            total_sum += number
        else:
            raise TypeError("Invalid argument, only integers and floats are allowed.")
    return f"The average is: {total_sum / len(numbers)}."


print(any_number(12, 90, 12, 34))
