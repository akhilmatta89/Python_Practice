

print("This is just for testing") #Just a print
print("The new line can be added using '\n' \n here iam a new line")

# The end keyword is used to specify the content that is to
# be printed at the end of the execution of the print() function.
# By default, it is set to “\n”, which leads to the change of line after the execution of print() statement.

print("Iam using the end keyword to add some thing at end ",end="Iam akhil")
print("")
print("Iam using the end keyword to add some thing at end", end="**")
print("Hey iam a new line")


name = "John"
age = 25
print(f"My name is {name} and I am {age} years old.")

name = "John"
age = 25
print("My name is {} and I am {} years old.".format(name, age))


name = "John"
age = 25
print("My name is %s and I am %d years old." % (name, age))



name = "John"
age = 25
print("My name is " + name + " and I am " + str(age) + " years old.")


from string import Template
name = "John"
age = 25
t = Template("My name is $name and I am $age years old.")
print(t.substitute(name=name, age=age))