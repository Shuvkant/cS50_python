
"""
3. Inheritance
Problem: Create an ElectricCar class that inherits from the Car class and has an additional
attribute battery_size.
"""


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_description(self):
        return f"{self.year} {self.make} {self.model}"


class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)
        self.battery_size = battery_size

    def get_battery_info(self):
        return f"This car has a {self.battery_size}-kWh battery."


my_electric_car = ElectricCar("Tesla", "Model S", 2024, 100)
print(my_electric_car.get_description())  # Output: 2024 Tesla Model S
print(my_electric_car.get_battery_info())
