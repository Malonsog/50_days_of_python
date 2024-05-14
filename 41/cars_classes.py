"""
Extra Challenge: Class of Cars
Create three classes of three car brands – Ford, BMW, and Tesla.
The attributes of the car's objects will be, model, color, year, transmission,
and whether the car is electric or not (Boolean value.) Consider using inheritance in your answer.

You will create one object for each car brand:
bmw1 : model: x6, Color: silver, Year: 2018, Transmission: Auto, Electric: False
tesla1: model: S, Color: beige, Year: 2017, Transmission: Auto, Electric: True
ford1 : model: focus, Color: white, Year: 2020, Transmission: Auto, Electric: False

You will create a class method, called print_cars that will be able to print out objects of the class.
For example, if you call the method on the ford1 object of the Ford class, your function should be able to print out
car info in this exact format:
car_model = focus
Color = White
Year = 2020
Transmission = Auto
Electric = False
"""


class Car:
    def __init__(self, model, color, year, transmission, electric: bool):
        self.model = model
        self.color = color
        self.year = year
        self.transmission = transmission
        self.electric = electric

    def print_car(self):
        print(f"| Model: {self.model}{' ' * (15 - len(self.model))}|")
        print(f"| Color: {self.color}{' ' * (15 - len(self.color))}|")
        print(f"| Year: {self.year}{' ' * 12}|")
        print(f"| Transmission: {self.transmission}{' ' * (8 - len(self.transmission))}|")
        print(f"| Electric: {self.electric}{' ' * (12 - len(str(self.electric)))}|")
        print(f"-------------------------")
        print("")


class Ford(Car):
    def __init__(self, model, color, year, transmission, electric: bool):
        super().__init__(model, color, year, transmission, electric)
        self.brand = "Ford"

    def print_car(self):
        print(f"-------------------------")
        print(f"| Brand: {self.brand}{' ' * 11}|")
        super().print_car()


class BMW(Car):
    def __init__(self, model, color, year, transmission, electric: bool):
        super().__init__(model, color, year, transmission, electric)
        self.brand = "BMW"

    def print_car(self):
        print(f"-------------------------")
        print(f"| Brand: {self.brand}{' ' * 12}|")
        super().print_car()


class Tesla(Car):
    def __init__(self, model, color, year, transmission, electric: bool):
        super().__init__(model, color, year, transmission, electric)
        self.brand = "Tesla"

    def print_car(self):
        print(f"-------------------------")
        print(f"| Brand: {self.brand}{' ' * 10}|")
        super().print_car()


# Creating class objects:
ford1 = Ford("Focus", "White", 2017, "Auto", False)
tesla1 = Tesla("S", "Grey", 2016, "Manual", True)
bmw1 = BMW("X6", "silver", 2018, "Auto", False)

# Calling the print_car method for each Car object:
ford1.print_car()
tesla1.print_car()
bmw1.print_car()
