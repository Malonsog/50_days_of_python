"""
Day 15: Same in Reverse
Write a function called same_in_reverse that takes a string and checks if the string reads the same in reverse.
If it is the same, the code should return True if not, it should return False.
For example, ‘dad’ should return True, because it reads the same in reverse.
"""


# This is my first attempt:
def same_in_reverse(string):
    if list(string) == list(reversed(string)):
        return True
    else:
        return False


print(same_in_reverse("dad"))


# Here is a better version using string slicing (more concise and efficient):
def same_in_reverse_v2(string):
    return string == string[::-1]


print(same_in_reverse_v2("dad"))
