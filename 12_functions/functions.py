"""
A function is a block of code that only runs when called. It can take input, execute code, and return output.
"""

def basic_greet_function(team_name):
    return f"Hello {team_name} Folks!"

def function_with_default_parameters(name='akhil'):
    return f"Hello {name}"

print(function_with_default_parameters())
print(function_with_default_parameters("Jaya"))

def function_with_default_and_normal_parameters(name, salary=1000):
    return f"Iam {name} and my salary is {salary}"

print(function_with_default_and_normal_parameters("akhil", 20000))
print(function_with_default_and_normal_parameters("Ben10"))


def function_with_variable_length_arguments_args(*args):
    """Python allows you to pass a variable number of arguments using *args for non-keyword arguments."""
    for each in args:
        print(each)
    return f"The arguments which you have passed are {args}"

print(function_with_variable_length_arguments_args("akhil","jaya","ishaanvik"))


def function_with_variable_length_arguments_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

function_with_variable_length_arguments_kwargs(name="akhil", age=30)
function_with_variable_length_arguments_kwargs(name="akhil", age=30, salary="20k")


def function_with_variable_length_arguments_kwargs_basic_test(**kwargs):
    print(kwargs.keys())
    print(kwargs.values())

    print(kwargs.get("name", "Not Provided"))
    print(kwargs.get("exp", "Not Provided"))

function_with_variable_length_arguments_kwargs_basic_test(name="akhil", age=30)
    