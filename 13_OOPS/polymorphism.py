"""
Polymorphism means "many forms". In Python, it refers to the same method name behaving differently
depending on the object calling it.

Types in Python:
Method Overriding – in Inheritance
Duck Typing – dynamic typing

"""

# Method Overriding


class Animal:
    def sound(self):
        print("Some animal sound")


class Dog(Animal):
    def sound(self):
        print("Bark")


class Cat(Animal):
    def sound(self):
        print("Meow")


for animal in [Animal(), Dog(), Cat()]:
    animal.sound()



#  Duck Typing
"""
In duck typing, the actual type doesn’t matter as long as the method exists:

"If it walks like a duck and quacks like a duck..."
"""

class Bird:
    def fly(self):
        print("Bird flies")

class Airplane:
    def fly(self):
        print("Airplane flies")

def lift_off(entity):
    entity.fly()

lift_off(Bird())      # Bird flies
lift_off(Airplane())  # Airplane flies

