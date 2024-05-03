"""
Day 26: Sort Words
Write a function called sort_words that takes a string of words as an argument, removes the whitespaces,
and returns a list of letters sorted in alphabetical order.
Letters will be separated by commas.
All letters should appear once in the list. This means that you sort and remove duplicates.
For example ‘love life’ should return as ['e,f,i,l,o,v'].
"""


def sort_words(string_of_words: str) -> list:
    letters = []
    for letter in string_of_words.replace(" ", ""):
        if letter not in letters:
            letters.append(letter)
    return sorted(letters)


# Version 2 using set() to eliminate duplicates and list comprehension:
def sort_words_2(string_of_words: str) -> list:
    return sorted([letter for letter in set(string_of_words.replace(" ", ""))])


test_phrase = "love life"
print(sort_words(test_phrase))
print(sort_words_2(test_phrase))
