class Person:
    def __init__(self, forename: str, surname: str, age:int=0) -> None:
        # Attribute being set explicitly on constructor
        self.surname: str = surname
        # We can create an attribute which isn't a constructor parameter. For instance, we don't want a person to be
        # able to have children at the time they are born, so we remove the children parameter from __init__
        self.children: list[Person] = []
        # Forename doesn't become an attribute - we can no longer access it directly outside of the constructor - but we
        # can still use it inside the constructor
        self.full_name: str = forename + " " + surname
        # Default values for attributes can be set as default values for function parameters
        self.age: int = age

        # The constructor is a function and can therefore have any code inside it, though it's rare that we want to do
        # anything other than set attributes. In real code a print statement like this might be in a separate function
        # so callers don't have to announce a birth every time they create a new object.
        print(self.full_name + " was born!")


# Creating an instance by calling the class name as a function causes the constructor `__init__` to be called with the
# same arguments, plus the implicit `self` argument
henry: Person = Person("Henry", "Tudor")
mary: Person = Person("Mary", "Tudor", age=16)
