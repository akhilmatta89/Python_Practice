# Print Statements:

# The print() function is used to display output in Python.
print("Hello, World!")

# Comments:
#
# Comments start with # and are ignored by the Python interpreter.
print("# This is a comment")

# Indentation:
#
# Python uses indentation to define blocks of code. Indent consistently to indicate code blocks.
# atleast one space is taken as indentation.
# best practice is to use 4 spaces.
if True:
    print("Indented block")

print("------------------------------------variables ---------------------------------------------")
# Variables:
# In Python, variables are created when you assign a value to it:
x = 5
y = "John"
print(x)
print(y)

# Variable Names:
# A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).
# Rules for Python variables:
# A variable name must start with a letter or the underscore character
# python identifier are the names which are used to define
# The assignment operator (=) is used to assign a value to a variable.
# The data type of the variable is determined by the value assigned to it.
# Python has no command for declaring a variable.
# A variable is created the moment you first assign a value to it.
# Variables do not need to be declared with any particular type and can even change type after they have been set.
# Variable names are case-sensitive.
# Variable Scope:
# A variable created inside a function is available inside that function.
# A variable created in the main body of the Python code is a global variable and belongs to the global scope.
# Global variables are available from within any scope, global and local.
# varibale name should not be a keyword
# should not seperate with space
# special symbols are not allowed

# You can change the value of a variable by reassigning it. Example:
x = 5
x = "John"
print(x)
# Assign values to multiple variables in a single line.
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)
# And you can assign the same value to multiple variables in one line.
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Swap the values of two variables without using a temporary variable.
x = "Python"
y = "C++"
x, y = y, x
print(x)
print(y)

# While Python doesn't have constants, it's a convention to use uppercase names for variables that shouldn't be changed.
PI = 3.14
print(PI)

# The del keyword can be used to delete a variable.
x = 5
print(x)
del x
try:
    print(x)
except Exception as ex:
    print(ex)

# Use the type() function to check the type of a variable.
x = 5
y = "John"
print(type(x))
print(type(y))

# keywords:
# key words are nothing but the reserved words in python
# To fetch the reserved key words in python
import keyword

print("______________________keywords")
for i in keyword.kwlist:
    print(i)

# global variables
# varibales which are created out side of a function are called global variables
# these are used both inside and outside of a function
print("________________global variable example_1")
x = "awesome"


def my_func():
    print("inside func iam", x)


class my_class():

    def my_func_2(self):
        print("inside func2 iam", x)


print("iam ", x)
my_func()
clss = my_class()
clss.my_func_2()

print("________________global variable example_2")

y = "world"


def sec_func():
    print("Hello ", y, "! This is sec_func() method")


def sec_func2():
    y = "akhil"
    global z
    z = "reddy"
    print("Hello ", y, "! This is sec_func2() method")


class my_class2():
    x = "jaya"

    def my_func_3(self):
        print("inside func3 iam", self.x)
        print(z)


sec_func()
sec_func2()
clsss = my_class2()
clsss.my_func_3()
