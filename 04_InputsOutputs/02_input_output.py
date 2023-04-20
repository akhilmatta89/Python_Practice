
myinp = input("Enter the input : ")  # This will be taken from keyboard
print(myinp)
myinp = "reddy"
print(myinp)

num = input("Enter number :")
print(num)
name1 = input("Enter name : ")
print(name1)

# Printing type of input value
print("type of number", type(num))
print("type of name", type(name1))

try:
    num = int(input("Enter a number: "))
    print(num, " ", type(num))
except ValueError as err:
    print("There is error with details : ", err)
finally:
    print("Some error occurred retry again by running file again")
