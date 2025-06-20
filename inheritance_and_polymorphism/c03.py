# dog class
class Dog:

    def __init__(self) -> None:
        pass

    def make_sound(self) -> None:
        print("Woof!")


# cat class
class Cat:

    def __init__(self) -> None:
        pass

    def make_sound(self) -> None:
        print("Meow!")


# bulldog class
class Bulldog(Dog):
    '''Bulldog class, inherits from Dog'''

    def __init__(self) -> None:
        super().__init__()

    def make_sound(self) -> None:  # OVERRIDING: Override method inherited from Dog
        print("Woof! I'm a Bulldog!")


# persian cat class
class PersianCat(Cat):
    '''Persian Cat class, inherits from Cat'''

    def __init__(self) -> None:
        super().__init__()

    def make_sound(self) -> None:  # OVERRIDING: Override method inherited from Cat
        print("Meow! I'm a Persian Cat!")


# Create instances of each class and add them to a list
# NOTE - the type annotation means the list contains objects that are either a Dog or Cat
#        Inheritance allows us to assign the parent class' type to an instance of a child class
my_pets: list[Dog | Cat] = [Dog(), Cat(), Bulldog(), PersianCat()]

# RUN-TIME POLYMORPHISM: one method interface can be called for objects of different classes
# This is type safe because both Dog and Cat have the make_sound() method.
for pet in my_pets:
    pet.make_sound()
