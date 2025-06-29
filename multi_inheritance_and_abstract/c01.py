class PrintableMixin:
    """
        String representation behaviour
    """
    # readable string representation
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}: {self.__dict__}"

class Person:
    """
        A person has a name and age
    """
    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age

class Car:
    """
        A car has a make and a model
    """
    def __init__(self, make: str, model: str) -> None:
        self.make: str = make
        self.model : str = model

# multiple inheritance
class PrintablePerson(Person, PrintableMixin):
    """
        Person class that inherits a string representation method
    """
    pass

# multiple inheritance
class PrintableCar(Car, PrintableMixin):
    """
        Car class that inherits a string representation method
    """
    pass

# we can treat the objects as their base class variants due to polymorphism
# we just added on a print behaviour
person: Person = PrintablePerson("Alice", 30)
car: Car = PrintableCar("Toyota", "Camry")

print(person)
print(car)
