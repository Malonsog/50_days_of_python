"""
Day 9: Biggest Odd Number
Create a function called biggest_odd that takes a string of numbers and returns the biggest odd number in the list.
For example, if you pass ‘23569’ as an argument, your function should return 9. Use list comprehension.
"""


numbers = "23569"
def biggest_odd(string_of_numbers):
    odds = [int(number) for number in list(string_of_numbers) if int(number) % 2 != 0]
    return max(odds)

print(biggest_odd(numbers))