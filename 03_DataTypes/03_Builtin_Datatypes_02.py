""" --------------------------  sequence Datatypes  ----------------------------------"""
# --------------------------string type --------------------------

name = "Akhil"
print(type(name))
print(name[2])
print(name[1::])
print(name[1:5])

othername = """Reddy saab """
print(othername)
print(othername[2:8])
print(name.split(","))
print(othername.split(" "))
print(othername * 2)
namelst = name.split()
namelst.append("reddy")
print(namelst)

# --------------------------Byte type --------------------------

elements = [10, 20, 30, 2, 40, 50, 5]
print(type(elements))
try:
    byteelem = bytes(elements)
except ValueError as e:
    print("The bytes should not contain negative values")
    count = 0
    for i in elements:
        if i > 0:
            count += 1
            pass
        else:
            elements.pop(count)
            count += 1
print(elements)
print(byteelem)
print("%%%%%%%%%%%%%",list(byteelem))
# Cannot modify or edit Byte types


# --------------------------ByteArray type --------------------------
elements = [10, 20, 30, 40, 50]  # Negative values are not allowed
print(type(elements))

bytearrayelements = bytearray(elements)
for i in bytearrayelements:
    print(i, ":", type(i))

mynewbyte = bytearrayelements.append(158)
print(mynewbyte)
for i in bytearrayelements:
    print(i, ":", type(i))

# --------------------------List type --------------------------
elements = [True, 10, -20, 30, 40, 50, "akhil", 100.95, [1, 2, 'reddy'], ("jaya", "reddy")]
print(elements[0])
print(elements[-1::])
print(elements[8::])
elements.append("HELLO")
elements.pop(1)
print(elements)

# --------------------------Tuple type --------------------------
# we cannot modify this datatype
tupelements = (True, 10, -20, 30, 40, 50, "akhil", 100.95, [1, 2, 'reddy'], ("jaya", "reddy"))
print(tupelements[0])
print(tupelements[-1::])
print(tupelements[8::])
try:
    tupelements.append("HELLO")
except AttributeError as err:
    print("appending is not supported", err)
try:
    tupelements.pop(1)
except AttributeError as err:
    print("popping is not supported", err)
print(tupelements)

# --------------------------Range type --------------------------
for i in range(10):
    print(i)