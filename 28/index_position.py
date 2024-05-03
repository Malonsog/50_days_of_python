"""
Day 28: Return Indexes
Write a function called index_position. This function takes a string as a parameter and
returns the positions or indexes of all lower letters in the string.
For example ‘LovE’ should return [1,2].
"""


def index_position(string: str) -> list[int]:
    index_list = []
    for i, letter in enumerate(string):
        if letter.islower():
            index_list.append(i)
    return index_list


test_string = "LovE"
print(index_position(test_string))
