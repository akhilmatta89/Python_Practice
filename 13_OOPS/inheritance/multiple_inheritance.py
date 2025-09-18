"""
When a child class inherits from more than one parent class, it’s called multiple inheritance.

Why use multiple inheritance?
To combine behaviors from different classes.
Useful when a class needs to have features from multiple sources.

"""

class Flyer:
    def fly(self):
        print("Flying in the sky")

class Swimmer:
    def swim(self):
        print("Swimming in the water")

class Duck(Flyer, Swimmer):
    def quack(self):
        print("Quack!")

d = Duck()
d.fly()      # from Flyer
d.swim()     # from Swimmer
d.quack()    # from Duck

class A:
    def greet(self):
        print("Hello from A")

class B:
    def greet(self):
        print("Hello from B")

class C(A, B):
    pass

c = C()
c.greet()  # Prints: Hello from A because A is first in inheritance list

