""" Builtin Datatypes are of 5 types.
    1. None type
    2. numeric types
    3. sequences
    4. sets
    5. mappings"""

"""--------------------------------None Type------------------------"""
a = None
print(a)
if 1 < 2:
    a = True
    print(type(a))
print(a)

"""--------------------------------Numeric Type------------------------"""

a = 10
print(type(a))  # int type

b = 10.5
print(type(b))  # float type

c = 10 + 2j
print(type(c))  # complex type

# -------------------------------- Converting Numeric Type datatypes-----------------------

print(float(a))
print(int(b))
print(complex(a))

""" --------------------------------Boolean Type------------------------"""

myboolval = False
if myboolval :
    print("This is true value")
else:
    print("This is false value")
