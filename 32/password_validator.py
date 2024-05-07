"""
Day 32: Password Validator
Write a function called password_validator. The function asks the user to enter a password.
A valid password should have at least one upper letter, one lower letter, and one number.
It should not be less than 8 characters long.
When the user enters a password, the function should check if the password is valid.
If the password is valid, the function should return the valid password.
If the password is not valid, the function should tell the users the errors in the password
and prompt the user to enter another password.
The code should only stop once the user enters a valid password. (use while loop).
"""


def password_validator():
    errors = []
    while True:
        password = input("Please enter your password: ")
        # Check length:
        if len(password) < 8:
            errors.append("Your password must be at least 8 characters long.")
        # Check if there is an uppercase char:
        if not any(char.isupper() for char in password):
            errors.append(f"Your password must have at least one uppercase character.")
        # Check if there is a lowercase char:
        if not any(char.islower() for char in password):
            errors.append(f"Your password must have at least one lowercase character.")
        # Check if there is a number:
        if not any(char.isdigit() for char in password):
            errors.append(f"Your password must have at least one number.")
        # Print the list of errors:
        if len(errors) > 0:
            print("Your password is not valid:")
            for error in errors:
                print(f"- {error}")
            print("")  # Add a blank line at the end.
            errors = []  # Clear the errors list.
        else:
            return f"Your password is: {password}"


print(password_validator())
