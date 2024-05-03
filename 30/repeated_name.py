"""
Day 30: Most Repeated Name
Write a function called repeated_name that finds the most repeated name in the following list:
name = ["John", "Peter", "John", "Peter", "Jones", "Peter"]
"""


def repeated_name(name_list: list[str]):
    name_counts = {}
    for name in name_list:
        if name in name_counts:
            name_counts[name] += 1
        else:
            name_counts[name] = 1
    most_common_name = max(name_counts, key=name_counts.get)
    max_count = name_counts[most_common_name]
    return f"The most common name is {most_common_name}, with {max_count} occurrences."


test_list = ["John", "Peter", "John", "Peter", "Jones", "Peter"]
print(repeated_name(test_list))
