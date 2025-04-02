# This conditional statements makes teh user to make decisions based on conditions
from pycparser.c_ast import Return


def is_even(num):
    if num %2 == 0: # Single If block will be used if you have only one condition
        return True

def return_even_or_odd(num):
    # In this scenario there is no need of else block we can directly return odd
    # For the sake of example iam adding it
    if num %2 == 0:
        return "even"
    else: # If 2 conditions are there we use else as well
        return "odd"

def animal_sounds(animal):
    # If we have 2 or more conditions we use if, elif, else syntax.
    if animal.lower() == "dog":
        return "Bow-Bow"
    elif animal.lower() == "cat":
        return "Meow-Meow"
    elif animal.lower() == "Buffalo":
        return "Ambhaaa :-)"
    else:
        return "The animal provided is not in list"

def check_number_is_divisible_by_five(num):
    # This example shows the nested if else statements
    if num > 0:
        if num %5 == 0:
            return f"{num} is divisible by 5"
        else:
            return f"{num} is not divisible by 5"
    else:
        return f"{num} should be greater than 0"

def ternary_if_operator(animal):
    # This shows about ternary conditional blocks
    # Means writing if-else in a single line
    return "Bow-Bow" if animal == "Dog" else "Not a Dog"

def using_logical_operators_in_conditional_statements(num):
    if num > 5 and num < 10:
        return "Number is in between 5-10"
    if num == 10 or num > 10 and num < 20:
        return "Number is 10 or in between 10-20"
    else:
        print("Number is Greater than 20")

def using_match(animal):
    # match and case are used same as if else
    match animal:
        case "Dog":
            return "Bow-Bow"
        case "Cat":
            return "Meow-Meow"

def using_lambda(animal):
    my_func = lambda animal: "Bow-Bow" if animal=="Dog" else "Meow-Meow"
    return my_func(animal)

# Using all()
def using_all(my_list):
    if all(i > 5 for i in my_list):
        return "All values are greater than 5"
    else:
        return "Something is not greater than 5"

def using_any(my_list):
    if any(i > 5 for i in my_list):
        return "Some Value Is Greater than 5"
    else:
        return "No value is greater than 5"