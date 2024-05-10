"""
Day 38: Guess a Number
Write a function called guess_a_number.
The function should ask a user to guess a randomly generated number.
If the user guesses a higher number, the code should tell them that the guess is too high,
if the user guesses low, the code should tell them that their guess is too low.
The user should get a maximum of three guesses. When the user guesses right, the code should declare them a winner.
After three wrong guesses, the code should declare them a loser.
"""
import random


def guess_a_number():
    random_number = random.randint(1, 9)
    attempts = 3
    print(f"Guess the number between 1 and 9, you have {attempts} attempts!")
    while attempts > 0:
        guess = int(input(f"Pick your guess: "))
        if guess == random_number:
            return f"You guessed it! The number is {random_number}!"
        else:
            attempts -= 1
            if guess < random_number:
                print(f"Your guess was too low.")
            elif guess < random_number:
                print(f"Your guess was too high.")
            if attempts > 0:
                print(f"You have {attempts} attempts left.")
    return f"Sorry, you ran out of attempts. The number was {random_number}."


print(guess_a_number())
