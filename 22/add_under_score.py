"""
Day 22: Add Under_Score
Create three functions.
The first called add_hash takes a string and adds a hash # between the words.
The second function called add_underscore removes the hash(#) and replaces it with an underscore ( _ ).
The third function called remove_underscore, removes the underscore and replaces it with nothing.
If you pass ‘Python’ as an argument for the three functions, and you call them at the same time,
like: "print(remove_underscore(add_underscore(add_hash('Python'))))", it should return ‘Python’.
"""


def add_hash(string: str) -> str:
    hashed_str = ""
    for word in string.split(" "):
        hashed_str += word + "#"
    return hashed_str.rstrip("#")


# Using the same approach as in the add_hash function:
def add_underscore(string: str) -> str:
    underscored_str = ""
    for word in string.split("#"):
        underscored_str += word + "_"
    return underscored_str.rstrip("_")


# Easier version using the replace() function:
def add_underscore_with_replace(string: str) -> str:
    return string.replace("#", "_")


# Using iteration with for loop:
def remove_underscore(string: str) -> str:
    no_spaces_str = ""
    for word in string.split("_"):
        no_spaces_str += word
    return no_spaces_str


# Using replace():
def remove_underscore_with_replace(string: str) -> str:
    return string.replace("_", "")

test_phrase = "This is a test."
print(f"Step one, adding a hash: {add_hash(test_phrase)}")
print(f"Step two, replacing hash with underscore: {add_underscore(add_hash(test_phrase))}")
print(f"Step three, removing the underscore: {remove_underscore(add_underscore(add_hash(test_phrase)))}")

print(f"Alternative version: {remove_underscore_with_replace(add_underscore_with_replace(add_hash(test_phrase)))}")
