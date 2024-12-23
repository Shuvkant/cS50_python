"""
1. Basic Class and Object
Problem: Create a Car class with attributes like brand and model. Then create an instance of this class.
"""


class Car:
    def __init__(self, brand, model):
        self.brand = brand,
        self.model = model


c1 = Car("BMW", "2000")

print(f"The car model is {c1.brand}")
print(f"The car brand is {c1.model}")
