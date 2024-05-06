"""
Day 31: Longest Word
Write a function that has one parameter and takes a list of words as an argument.
The function returns the longest word from the list. Name the function longest_word.
The function should return the longest word and the number of letters in that word.
For example, if you pass [‘Java, ‘JavaScript’, ‘Python’], your function should return
[10, JavaScript] as the longest word.
"""


def longest_word(list_of_words: list[str]) -> list:
    longest = ""
    for word in list_of_words:
        if len(word) > len(longest):
            longest = word
    return [len(longest), longest]


# Using dictionary comprehension:
def longest_word_2(list_of_words: list[str]) -> list:
    word_dict = {word: len(word) for word in list_of_words}
    longest = max(word_dict, key=word_dict.get)
    longest_length = word_dict[longest]
    return [longest_length, longest]


test_list = ["Java", "JavaScript", "Python"]
print(longest_word(test_list))
print(longest_word_2(test_list))
