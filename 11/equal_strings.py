"""
Day 11: Are They Equal?
Write a function called equal_strings. The function takes two strings as arguments and compares them.
If the strings are equal (if they have the same characters and have equal length), it should return True,
if they are not, it should return False. For example, ‘love’ and ‘evol’ should return True.
"""


def equal_strings(str_1, str_2):
    if len(str_1) == len(str_2):
        if list(str_1.lower()).sort() == list(str_2.lower()).sort():
            return True
        else:
            return False
    else:
        return False


print(equal_strings("love", "evol"))
