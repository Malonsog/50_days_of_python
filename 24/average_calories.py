"""
Day 24: Average Calories
Create a function called average_calories that calculates the average calories intake of a user.
The function should ask the user to input their calories intake for any number of days
and once they hit ‘done’ it should calculate and return the average intake.
"""


def average_calories():
    scores = []
    while True:
        score = input(f"Enter the amount of calories and hit 'enter' for each meal (write 'done' when you are finished): ")
        if score.lower() == "done":
            break
        scores.append(int(score))
    return f"Average calories intake is {sum(scores) / len(scores):.2f}"


print(average_calories())
