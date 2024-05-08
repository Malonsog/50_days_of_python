"""
Day 35: Pangram
Write a function called check_pangram that takes a string and checks if it is a pangram.
A pangram is a sentence that contains all the letters of the alphabet.
If it is a pangram, the function should return True, otherwise, return False.
The following sentence is a pangram so it should return True:

'the quick brown fox jumps over a lazy dog'
"""
import string


def check_pangram(sentence: str) -> bool:
    alphabet = list(string.ascii_lowercase)
    if alphabet == sorted(set(sentence.replace(" ", ""))):
        return True
    else:
        return False


test_sentence = "the quick brown fox jumps over a lazy dog"
print(check_pangram(test_sentence))
