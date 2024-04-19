"""
Day 10: Hide my Password
Write a function called hide_password that takes no parameters.
The function takes an input( a password) from a user and returns a hidden password.
For example, if the user enters ‘hello’ as a password the function should return ‘****’ as a password
and tell the user that the password is 4 characters long.
"""


import getpass
def hide_password():
    password = getpass.getpass("Insert your password: ")
    password_length = len(password)
    asterisks = "*" * password_length
    return f"Your password '{asterisks}' is {password_length} characters long."


print(hide_password())
