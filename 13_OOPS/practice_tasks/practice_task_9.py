"""
Practice Task 10: Polymorphism
Create a base class Shape with a method area() that prints "Calculating area..."

Create two subclasses:

Rectangle with its own area() → "Area = length × width"

Circle with its own area() → "Area = π × radius²"

Iterate over both objects and call area() to demonstrate polymorphism.
"""

class Shape:
    def area(self):
        print("Calculating area...")

class Rectangle(Shape):
    def area(self):
        print("Area = length × width")

class Circle(Shape):
    def area(self):
        print("Area = π × radius²")

class Square(Shape):
    pass

for each_class in [Shape(), Rectangle(), Circle(), Square()]:
    each_class.area()