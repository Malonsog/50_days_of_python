"""
Day 14: Flatten the List
Write a function called flat_list that takes one argument, a nested list.
The function converts the nested list into a one-dimension list. For example [[2,4,5,6]] should return [2,4,5,6].
"""

def flat_list(nested_list):
    flattened_list = []
    for item in nested_list:
        if isinstance(item, list):
            flattened_list.extend(flat_list(item))
        else:
            flattened_list.append(item)
    return flattened_list


print(flat_list([[2,4,5,6], [8, 11, 15], [5]]))
