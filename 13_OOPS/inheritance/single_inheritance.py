"""
Practice Task 5 (Single Inheritance):
Create a base class Person with:

Method introduce() → prints "Hi, I'm a person"

Create a derived class Student that:

Inherits Person

Has method study() → prints "I'm studying"
"""

class Person:

    def introduce(self):
        print("Hi, I'm a person")

class Student(Person):
    def study(self):
        print("I'm studying")

s = Student()
s.introduce()
s.study()