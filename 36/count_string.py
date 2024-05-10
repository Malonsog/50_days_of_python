"""
Day 36: Count String
Write a function called count that takes one argument a string, and returns a dictionary of how many times
each element appears in the string. For example ‘hello’ should return:
{‘h’:1,’e’: 1,’l’:2, ‘o’:1}.
"""


def count(string: str):
    count_dict = {}
    for i in string:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    return count_dict


test_string = "hello"
print(count(test_string))
