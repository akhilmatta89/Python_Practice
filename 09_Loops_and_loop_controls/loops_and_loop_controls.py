""" The for loop iterates over sequences like lists, tuples, dictionaries, and strings."""

def basic_for_loop():
    for i in range(1,11):
        print(i)

def iterating_over_list(my_list):
    for i in my_list:
        print(i)

def iterating_ver_tuple(my_tuple):
    for i in my_tuple:
        print(i)

def iterating_over_a_string(mystr):
    for i in mystr:
        print(i)


""" While Loops till the condition is met, once the condition is met it stops looping through"""

def basic_while_loop():
    num = 0
    while num <= 5:
        print(num)
        num+=1

def user_input_loop():
    password = ("")
    while password != "Password@123":
        password = str(input("Enter Password: "))
    print("Access Granted")


"""Loop Control Statements"""
# --------------------- Break ------------------------------
def using_break():
    for i in range(1,10):
        if i == 6:
            break
        print(i)

# Pass and break works as same but pass is used to write some future code
# and continue is to skip current iteration and continue
# ---------------------- Pass -------------------------------
def using_pass():
    for i in range(1,10):
        if i == 5:
            pass
        else:
            print(i)

# ----------------------- Continue -------------------------------
def using_continue():
    for i in range(1,10):
        if i == 5:
            continue
        else:
            print(i)

# Nested Loops
def using_nested_loops():
    for i in range(1,4):
        for j in range(1,4):
            print(f"({i},{j})")


def using_else_with_loop():
    for num in range(1, 6):
        if num == 7:
            break
    else:
        print("Loop completed successfully!")

# using zip to iterate over 2/more iterables
def using_zip():
    my_list = [1,2,3]
    my_list_2 = [4,5,6,7]
    my_tuple = (8,9,10)
    for ml_1, ml_2, mt_1 in zip(my_list, my_list_2,my_tuple):
        print(f"{ml_1},{ml_2},{mt_1}")

using_zip()