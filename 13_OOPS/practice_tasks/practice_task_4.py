"""
Practice Task 4:
Create an abstract class Animal with:

Abstract method: sound()

Normal method: eat() that prints "Animals eat food"

Then, create a Dog class that:

Inherits from Animal

Implements the sound() method → prints "Bark!"

"""
from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

    def eat(self):
        print("Animals eat food")

class Dog(Animal):
    def sound(self):
        print("Bark!")


d = Dog()
d.sound()
d.eat()