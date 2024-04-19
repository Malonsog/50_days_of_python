"""
Day 8: Odd and Even
Write a function called odd_even that has one parameter and takes a list of numbers as an argument.
The function returns the difference between the largest even number in the list and the smallest odd number in the list.
For example, if you pass [1,2,4,6] as an argument the function should return 6 -1= 5.
"""


numbers_list = [1, 2, 3, 4, 5, 5, 6]

def odd_even(list):
    max_even = max([number for number in list if number % 2 == 0])
    min_odd = min([number for number in list if number % 2 != 0])
    return max_even - min_odd

print(odd_even(numbers_list))