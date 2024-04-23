"""
Day 21: List of Tuples
Write a function called make_tuples that takes two lists, equal lists, and combines them into a list of tuples.
For example if list a is [1,2,3,4] and list b is [5,6,7,8], your function should return [(1,5),(2,6),(3,7),(4,8)].
"""


# Version 1:
def make_tuples(list_a, list_b):
    list_of_tuples = []
    for i in range(len(list_a)):
        new_tuple = (list_a[0 + i],) + (list_b[0 + i],)
        list_of_tuples.append(new_tuple)
    return list_of_tuples


print(make_tuples([1, 2, 3, 4], [5, 6, 7, 8]))


# Version 2 using list comprehension:
def make_tuples_v2(list_a, list_b):
    list_of_tuples = [(item,) + (list_b[list_a.index(item)],) for item in list_a]
    return list_of_tuples


print(make_tuples_v2([1, 2, 3, 4], [5, 6, 7, 8]))
