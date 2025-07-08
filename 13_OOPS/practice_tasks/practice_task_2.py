"""
Practice Task 2:
Create a class Laptop that has:

Class attribute: category = "Electronics"

Instance attributes: brand, model, price

Method: details() that prints all info
"""

class Laptop:
    category = "Electronics"

    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def details(self):
        print(f"the {self.category} brand is {self.brand} and model {self.model} with price {self.price}")


l1 = Laptop("Dell","Latitude", 5200)
l1.details()