# The Callable type annotation is used to write function types
from typing import Callable

# Since functions are first class objects, they also have a type
# When we call func, we provide NO arguments and it returns nothing
# Hence the type for func is Callable[[], None] which means func is a function that takes no arguments and returns None.
def run_three_times(func: Callable[[], None]) -> None:
    for i in range(3):
        # "func" isn't the name of a function, but is a variable which will contain a function
        func()


def say_hello() -> None:
    print("Hello world!")


def greet_user() -> None:
    name = input("What is your name? ")
    print(f"Hello {name}!")


def say_goodbye() -> None:
    print("Goodbye")


# No brackets here
# Putting brackets would call the function and its value would be the return type, in this case None.
# We want to be able to call the function, hence we do not put brackets.
phrase_functions: list[Callable[[], None]] = [say_hello, greet_user, say_goodbye]

print("Enter 1 for a generic greeting, 2 for a personalised greeting, and 3 for a valediction")
option = int(input()) - 1
run_three_times(phrase_functions[option])
