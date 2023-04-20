x = 10  #int
y = 20.5 #float
z = 1+10j #complex

print(type(x))
print(type(y))
print(type(z))


# conversion

print(float(x))
print(int(y))
# print(int(z))  ----> This gives error as we cannot convert complex to int
print(complex(x))
print(complex(y))


# Random module
import random

print(random.randint(1,10))
print(random.random())  # This gives values from 0-1
random.seed(10)
print(random.random())


# Python Casting

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

print(x)
print(y)
print(z)

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

print(x)
print(y)
print(z)
print(w)