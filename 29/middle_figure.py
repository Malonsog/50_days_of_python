"""
Day 29: Middle Figure
Write a function called middle_figure that takes two parameters a and b. The two parameters are strings.
The function joins the two strings and finds the middle element.
If the combined string has a middle element, the function should return the element,
otherwise, return ‘no middle figure’.
Use ‘ make love’ as an argument for a and ‘not wars’ as an argument for b.
Your function should return ‘e’ as the middle element. Whitespaces should be removed.
"""


def middle_figure(a: str, b: str) -> str:
    c = (a + b).replace(" ", "")
    if len(c) % 2 == 0:
        return "No middle figure"
    else:
        i = len(c) // 2
        return f"The middle figure is '{c[i]}'"


a_string = "make love"
b_string = "not wars"
print(middle_figure(a_string, b_string))
