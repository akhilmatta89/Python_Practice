"""
What are Dunder Methods?
"Dunder" means double underscore (e.g. __init__, __str__, __add__).

They allow custom behavior for your objects:

Object construction (__init__)

Object display (__str__)

Comparison (__eq__, __lt__)

Arithmetic (__add__, __mul__)

Length, item access, etc.

"""


#  Example 1: __init__ and __str__

class Book:
    def __init__(self, title, author):  # Constructor
        self.title = title
        self.author = author

    def __str__(self):  # String representation
        return f"'{self.title}' by {self.author}"


# Creating an object
b1 = Book("The Alchemist", "Paulo Coelho")

# Without __str__:
# print(b1) → <__main__.Book object at 0x...>

# With __str__:
print(b1)  # Output: 'The Alchemist' by Paulo Coelho
