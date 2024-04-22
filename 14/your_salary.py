"""
Extra Challenge: Teacher’s Salary
A school has asked you to write a program that will calculate teachers' salaries.
The program should ask the user to enter the teacher’s name, the number of periods taught in a month, and the rate per period.
The monthly salary is calculated by multiplying the number of periods by the monthly rate.
The current monthly rate per period is $20. If a teacher has more than 100 periods in a month,
everything above 100 is overtime. Overtime is $25 per period.
For example, if a teacher has taught 105 periods, their monthly gross salary should be 2,125.

Write a function called your_salary that calculates a teacher’s gross salary.
The function should return the teacher’s name, periods taught, and gross salary.
Here is how you should format your output:

Teacher: John Kelly
Periods: 105
Gross salary:2,125
"""


def your_salary():
    overtime_rate = 25.0
    teachers_name = input("Please enter the teacher's name: ")
    # Validate the number of periods input:
    while True:
        try:
            number_of_periods = int(input("Please enter the number of periods taught per month: "))
            if number_of_periods <= 0:
                raise ValueError("please enter a positive number of periods")
            else:
                break
        except ValueError as e:
            if "invalid literal for int() with base 10" in str(e):
                print("Invalid input, please enter a number of periods (e.g., 10, 20).")
            else:
                print(f"Invalid input, {e}.")
    # Validate the rate per period input:
    while True:
        try:
            rate = float(input("Please enter the rate per period: "))
            if rate <= 0:
                raise ValueError("please enter a positive rate value")
            else:
                break
        except ValueError as e:
            if "could not convert string to float" in str(e):
                print("Invalid input, please enter a number for the rate value.")
            else:
                print(f"Invalid input, {e}.")

    if number_of_periods > 100:
        salary = (100 * rate) + ((number_of_periods - 100) * overtime_rate)
    else:
        salary = number_of_periods * rate
    return f"""
    Teacher: {teachers_name}
    Periods: {number_of_periods}
    Gross salary: ${salary:,}
    """


print(your_salary())
