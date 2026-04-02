class Car:
    def __init__(self, make, model, year):
        # Initialize the attributes
        self.make = make
        self.model = model
        self.year = year
    
    def describe_car(self):
        # Print information in the format: Year Make Model
        print("{} {} {}".format(self.year, self.make, self.model))

# Task 2
# Create an instance of the Car class with the following attributes and call describe_car method:
# - Make: Toyota, Model: Corolla, Year: 2020

Car1 = Car("Toyota", "Corolla", 2020)
Car1.describe_car()  # Output: 2020 Toyota Corolla
