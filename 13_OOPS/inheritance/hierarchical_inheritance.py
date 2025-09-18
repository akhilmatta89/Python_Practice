"""
When multiple classes inherit from the same parent class, it’s called hierarchical inheritance.

"""

class Vehicle:
    def start(self):
        print("Vehicle started")

class Car(Vehicle):
    def drive(self):
        print("Car is driving")

class Bike(Vehicle):
    def ride(self):
        print("Bike is riding")

c = Car()
c.start()
c.drive()

b = Bike()
b.start()
b.ride()
