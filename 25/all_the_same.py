"""
Day 25: All the Same
Create a function called all_the_same that takes one argument, a string, a list, or a tuple
and checks if all the elements are the same.
If the elements are the same, the function should return True. If not, it should return False.
For example, [‘Mary’, ‘Mary’, ‘Mary’] should return True.
"""


def all_the_same(elements):
    for i in range(len(elements) - 1):
        if elements[i] != elements[i + 1]:
            return False
    return True


def all_the_same_2(elements):
    for i, element in enumerate(elements):
        if elements[i] != elements[0]:
            return False
    return True


def all_the_same_3(elements):
    return all(i == elements[0] for i in elements)


test = ["Mary", "Mary", "Mary"]
print(all_the_same(test))
print(all_the_same_2(test))
print(all_the_same_3(test))
