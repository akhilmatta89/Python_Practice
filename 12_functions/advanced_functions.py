# lambda functions
# Lambda functions are small, one-line functions that are useful for short-term use, especially in functional programming.

my_lambda_function = lambda x:x**2
print(my_lambda_function(2))

my_other_lambda_function = lambda a,b : a*b
print(my_other_lambda_function(10,20))


# A recursive function is a function that calls itself.
# It's often used in problems that can be broken down into smaller, similar problems.
def recursive_functions():
    password = str(input("Enter the password"))
    if password != "Password@123":
        recursive_functions()
    else:
        print("Congrats! Password updated successfully")


def function_returning_multiple_values():
    return "a","b","c","d"

def min_max(numbers):
    return min(numbers), max(numbers)

# Functions that take other functions as arguments or return functions are called higher-order functions.
def higher_order_functions(a,b,operation):
    return operation(a,b)

print(higher_order_functions(10,30, lambda a,b:a*b))

def function_with_annotations(a: str,b: str) -> str:
    return f"My full name is {a} {b}"

print(function_with_annotations("akhil","reddy"))