"""
Day 33: List Intersection
Write a function called inter_section that takes two lists and finds the intersection
(the elements that are present in both lists). The function should return a tuple of intersections.
Use list comprehension in your solution. Use the lists below. Your function should return (30, 65, 80).
list1 = [20, 30, 60, 65, 75, 80, 85] list2 = [ 42, 30, 80, 65, 68, 88, 95]
"""


# Using list comprehension and returning a tuple:
def inter_section(list_a: list, list_b: list):
    intersection = [element for element in list_a if element in list_b]
    return tuple(intersection)


# Using set and & operator:
def inter_section_2(list_a: list, list_b: list):
    intersection = list(set(list_a) & set(list_b))
    return sorted(intersection)


list1 = [20, 30, 60, 65, 75, 80, 85]
list2 = [42, 30, 80, 65, 68, 88, 95]
print(inter_section(list1, list2))
print(inter_section_2(list1, list2))
