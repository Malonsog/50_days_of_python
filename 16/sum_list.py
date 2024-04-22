"""
Day 16: Sum the List
Write a function called sum_list with one parameter that takes a nested list of integers as an argument
and returns the sum of the integers.
For example, if you pass [[2, 4, 5, 6], [2, 3, 5, 6]] as an argument your function should return a sum of 33.
"""


# Based on the "flat_list" function from day 14.
def sum_list(nested_list):
    total_sum = 0
    for item in nested_list:
        if isinstance(item, list):
            # Recursive call for nested lists
            total_sum += sum_list(item)
        else:
            # Add individual integers
            total_sum += item
    return total_sum


print(sum_list([[2, 4, 5, 6], [2, 3, 5, 6]]))
