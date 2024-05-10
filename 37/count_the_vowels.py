"""
Day 37: Count the Vowels
Create a function called count_the_vowels.
The function takes one argument, a string, and returns the number of vowels in the string.
For example ‘hello’ should return 2 vowels.
If a vowel appears in a string more than once it should be counted as one.
For example, ‘saas’ should return 1 vowel. Your code should count lowercase and uppercase vowels.
"""


def count_the_vowels(string: str) -> int:
    vowels = ["a", "e", "i", "o", "u"]
    vowels_in_string = []
    for letter in string:
        if letter.lower() in vowels:
            vowels_in_string.append(letter.lower())
    return len(set(vowels_in_string))

test_string = "hello"
print(count_the_vowels(test_string))
