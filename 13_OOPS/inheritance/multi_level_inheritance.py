"""
In multilevel inheritance, a class inherits from a derived class, forming a chain.


"""

class Animal:
    def breathe(self):
        print("Breathing...")

class Mammal(Animal):
    def walk(self):
        print("Walking...")

class Human(Mammal):
    def speak(self):
        print("Speaking...")

h = Human()
h.breathe()  # from Animal
h.walk()     # from Mammal
h.speak()    # from Human
