"""
Day 7: A String Range
Write a function called string_range that takes a single number and returns a string of its range.
The string characters should be separated by dots(.) For example, if you pass 6 as an argument,
your function should return ‘0.1.2.3.4.5’.
"""


def string_range():
    number = int(input("Insert a number: "))
    string = ".".join(str(element) for element in range(0, number))
    return string

print(string_range())