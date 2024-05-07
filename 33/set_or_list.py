"""
Extra Challenge: Set or list
You want to implement a code that will search for a number in a range.
You have a decision to make as to whether to store the number in a set or a list.
Your decision will be based on time. You have to pick a data type that executes faster.
You have a range and you can either store it in a set or a list depending on which one executes faster
when you are searching for a number in the range.

See below:
a = range(10000000)
x = set(a)
y = list(a)

Let’s say you are looking for a number 9999999 in the range above.
Search for this number in the list and the set.
Your challenge is to find which code executes faster.
You will pick the one that executes quicker, lists, or sets. Run the two searches and time them.
"""
import timeit

test_set = """
a = range(10000000)
x = set(a)
i = 9999999

if i in x:
    True
"""

test_list = """
a = range(10000000)
x = list(a)
i = 9999999

if i in x:
    True
"""

print(f"Time test for set: {timeit.timeit(stmt=test_set, number=5)}")
print(f"Time test for list: {timeit.timeit(stmt=test_list, number=5)}")
