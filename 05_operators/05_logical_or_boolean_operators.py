x = 10
y = 20
z = 30

# AND operator

if x < 20 and y > x:
    print("some blah and successful")
if (x < 20) & (y > x):
    print("some blah and successful")

if x > z or x < y:
    print("some blah or successful")

if (x > z) | (x < y):
    print("some blah or successful")
else:
    print("-----------")

a = None
if not a:
    print("some blah not successful")