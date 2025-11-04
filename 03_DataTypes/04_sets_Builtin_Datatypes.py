""" --------------------------  sequence Datatypes  ----------------------------------"""

# SET
# FROZENSET
#----------------------------------- SET ------------------------------------------------
myset = {10, 20, 30, 40, 50, 10} # This will return unordered collection, no duplicates are allowed
print(type(myset))
print(myset)

strset = set("hello")
print(strset)


lstset = [10, 20, 30, 40, 50, 10]
lstset2=set(lstset)
print(lstset2)

#slicing or indexing we cannot do as it is unordered
lstset2.update([1000,2000])
print(lstset2)

lstset2.remove(2000)
print(lstset2)


#----------------------------------- FROZEN SET ------------------------------------------------

myfrznset = {10, 20, 30, 40, 50, 10} #This cannot be modified
frznset = frozenset(myfrznset)
print(frznset)
try:
    frznset.update([1000,2000])
except AttributeError as err:
    print("modifying is not supported", err)


# Using frozenset as dictionary key
d = {frozenset([1, 2]): "pair"}
print(d[frozenset([1, 2])])  # ✅
print(d)