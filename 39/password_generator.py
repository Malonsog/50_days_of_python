"""
Day 39: Password Generator
Create a function called generate_password that generates any length of password for the user.
The password should have a random mix of upper letters, lower letters, numbers, and punctuation symbols.
The function should ask the user how strong they want the password to be.
The user should pick from - weak, strong, and very strong.
If the user picks weak, the function should generate a 5 character long password.
If the user picks strong, generate an 8 character password and if they pick very strong, generate a 12 character password.
"""
import random
import string


def generate_password():
    password_length = 0
    print(f"Welcome to the secure password generator!")
    print(f"Options:")
    print(f"A - Weak")
    print(f"B - Strong")
    print(f"C - Very strong")
    print(f"")
    while True:
        try:
            strength = input("Select the strength for your password: ")
            if strength.lower() not in ("a", "b", "c"):
                raise ValueError(f"Invalid input.")
            else:
                break
        except ValueError as e:
            print(f"{e} Please select a valid operation.")
    if strength.lower() == "a":
        password_length = 5
    elif strength.lower() == "b":
        password_length = 8
    elif strength.lower() == "c":
        password_length = 12

    # Define the amount of each type of character
    uppercase_count = password_length // 4
    lowercase_count = password_length // 4
    digit_count = password_length // 4
    punctuation_count = password_length // 4

    # Ensure at least the defined amount from each category
    uppercase = ''.join(random.choices(string.ascii_uppercase, k=uppercase_count))
    lowercase = ''.join(random.choices(string.ascii_lowercase, k=lowercase_count))
    digit = ''.join(random.choices(string.digits, k=digit_count))
    punctuation = ''.join(random.choices(string.punctuation, k=punctuation_count))

    # Combine all characters
    characters = string.ascii_letters + string.digits + string.punctuation

    # Fill the remaining length with random characters
    remaining_length = password_length - (uppercase_count + lowercase_count + digit_count + punctuation_count)
    other_characters = ''.join(random.choices(characters, k=remaining_length))

    # Concatenate all characters and shuffle them
    password = ''.join(random.sample(uppercase + lowercase + digit + punctuation + other_characters, password_length))
    return f"Your password is: {password}"


print(generate_password())
