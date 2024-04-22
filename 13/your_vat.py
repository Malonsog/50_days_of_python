"""
Day 13: Pay Your Tax
Write a function called your_vat. The function takes no parameter.
The function asks the user to input the price of an item and VAT (vat should be a percentage).
The function should return the price of the item plus VAT. If the price is 220 and,
VAT is 15% your code should return a vat inclusive price of 253. Make sure that your code can handle ValueError.
Ensure the code runs until valid numbers are entered. (hint: Your code should include a while loop).
"""


def your_vat():
    while True:
        user_input = input("Indicate the price of the item: ")
        try:
            price = float(user_input)
            if price <= 0:
                raise ValueError("Please enter a positive number.")
            else:
                price_with_vat = price * 1.15
                return f"The final price is : ${price_with_vat:.2f}."
        except ValueError:
            print(f"Invalid input: Please enter a positive number in numeric format (e.g., 10.50).")


print(your_vat())
