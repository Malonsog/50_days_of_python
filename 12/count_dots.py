"""
Day 12: Count the Dots
Write a function called count_dots. This function takes a string separated by dots as a parameter
and counts how many dots are in the string.
For example, ‘h.e.l.p.’ should return 4 dots, and ‘he.lp.’ should return 2 dots.
"""


def count_dots(string):
    count = [char for char in string if char == "."]
    return len(count)


print(count_dots("h.e.l.p."))
