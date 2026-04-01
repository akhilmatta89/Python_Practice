from datetime import datetime


def wish():
    hour = datetime.now().hour
    if hour < 12:
        print("Good Morning")
    elif 12 <= hour < 17:
        print("Good Afternoon")
    else:
        print("Good Night")


def add_greet(base_func):
    def additional_greet(*args):
        print("iam a decorator function")
        wish()  # return it
        result = base_func(*args)  # store result
        return result

    return additional_greet


@add_greet
def greet(name):
    return f"Hi {name} nice to meet you"


print(greet("akhil"))

print("------------------------------------------------------------------------------------------------")


# Authentication decorator

class AuthException(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "To perform this you need to be a admin"


def authenticate(base_func):
    def add_auth(**kwargs):
        print("iam decorator")
        if kwargs["user_name"] != "Admin":
            raise AuthException
        base_func(**kwargs)

    return add_auth


@authenticate
def hit_home(user_name, name="Dravid"):
    print(f"welcome to home {name}")


hit_home(user_name="Admin")


print("---------------------------------------------decorator chaining---------------------------------------------------")

def jaya_mom(base_func):
    def add_jaya_mom(name):
        print(f'jaya mom of {name}')
        base_func(name)
    return add_jaya_mom

def akhil_dad(base_func):
    def add_akhil_dad(name):
        print(f'akhil dad of {name}')
        base_func(name)
    return add_akhil_dad

@akhil_dad
@jaya_mom
def ishaanvik_reddy(name):
    print('iam a cute boy')


ishaanvik_reddy("Ishaanvik Reddy")