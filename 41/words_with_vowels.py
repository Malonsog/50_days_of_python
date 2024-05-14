"""
Day 41: Only Words with Vowels
Create a function called words_with_vowels, this function takes a string of words and returns a list of only words
that have vowels in them. For example ‘ You have no rhythm’ should return [‘You’,’have’, ‘no’].
"""


def words_with_vowels(string: str) -> list:
    with_vowels = []
    for word in string.split():
        for letter in word:
            if letter.lower() in "aeiou" and word not in with_vowels:
                with_vowels.append(word)
    return with_vowels


test_string = "You have no rhythm"
print(words_with_vowels(test_string))
