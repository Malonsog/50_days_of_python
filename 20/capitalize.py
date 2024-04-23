"""
Day 20: Capitalize First Letter
Write a function called capitalize.
This function takes a string as an argument and capitalizes the first letter of each word.
For example, ‘i like learning’ becomes ‘I Like Learning’.
"""


# Version 1 using list comprehension:
def capitalize(string_of_words):
    word_list = [(word[0].upper() + word[1:]) for word in string_of_words.split(" ")]
    capitalized_words = " ".join(word_list)
    return capitalized_words


print(capitalize("i like learning"))


# Version 2 using list comprehension:
def capitalize_v2(string_of_words):
    capitalized_words = ""
    for word in string_of_words.split(" "):
        capitalized_word = word[0].upper() + word[1:] + " "
        capitalized_words += capitalized_word
    return capitalized_words.rstrip()


print(capitalize_v2("i like learning"))


# Version 3 using built-in function (boring):
def capitalize_v3(string_of_words):
    return string_of_words.title()


print(capitalize_v3("i like learning"))