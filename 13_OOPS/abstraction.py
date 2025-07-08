"""
Hiding the implementation and showing only essential features.

When you use a TV remote, you just press buttons (interface),
but you don’t care how it works internally (implementation). That’s abstraction.

In Python, Abstraction is achieved using:
Abstract Classes (via abc module)
Abstract Methods (must be implemented in child classes)
"""

from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start_engine(self):
        print("Car engine not started!")

    def description(self):
        print("Vehicles have engines.")


class Car(Vehicle):
    def start_engine(self):
        print("Car engine started!")


#v = Vehicle()     # ❌ Error: Can't instantiate abstract class
my_car = Car()  # ✅ Subclass must implement all abstract methods
my_car.start_engine()
my_car.description()
