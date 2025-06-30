from typing import Callable

def create_printer(string: str) -> Callable[[], None]:
    def printer() -> None:
        print(string)

    return printer

# Callable[..., object] is the type annotation for any function
# because basically all functions have a qualname
def get_function_name(func: Callable[..., object] ) -> str:
    return func.__qualname__


functions: list[Callable[..., object]] = [int, print, len]
option: int = int(input("Enter the number of a function to use: ")) - 1

___: Callable[..., object] = functions[option]
name: str = ___(func)
create_printer(___)__

