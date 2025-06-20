class Animal:
    '''Animal class as base class'''

    def __init__(self, name: str, species: str) -> None:
        self.name: str = name
        self.species: str = species
        self.__age: int = 0  # Private property

    def make_sound(self) -> str:
        return "Some generic animal sound"

    def age(self) -> int:
        return self.__age


class Mammal(Animal):
    '''Mammal class inherits from Animal class'''

    def __init__(self, name: str, species: str, is_warm_blooded:bool=True) -> None:
        super().__init__(name, species)
        self.is_warm_blooded: bool = is_warm_blooded

    def give_birth(self) -> str:
        return "Gives birth to live young"

    def age(self) -> int:
        return self.__age


class Reptile(Animal):
    '''Reptile class inherits from Animal class'''

    def __init__(self, name: str, species: str, is_venomous:bool=False) -> None:
        super().__init__(name, species)
        self.is_venomous: bool = is_venomous

    def lay_eggs(self) -> str:
        return "Lays eggs"


class Dog(Mammal):
    '''Dog class inherits from Mammal class'''

    def __init__(self, name: str, breed: str) -> None:
        super().__init__(name, species="Dog")
        self.breed: str = breed

    def make_sound(self) -> str:  # Overriding method
        return "Bark"


# Create instances of each class
generic_animal: Animal = Animal("GenericAnimal", "GenericSpecies")
mammal: Mammal = Mammal("MammalAnimal", "GenericMammalSpecies")
dog: Dog = Dog("Buddy", "Golden Retriever")
reptile: Reptile = Reptile("Slither", "Snake", is_venomous=True)

# An animal has a name, species, and can make a sound
print(generic_animal.name, generic_animal.species, generic_animal.make_sound())

# A mammal inherits the name, species, and make sound properties/methods from animal
# And has an extra method give birth
print(f"{mammal.name}, {mammal.species}, {mammal.make_sound()}, {mammal.give_birth()}")

# A dog has the same properties and methods as the mammal but the make_sound() method is overridden
# And it has an extra property called breed
print(f"{dog.name}, {dog.species}, {dog.make_sound()}, {dog.give_birth()}")

# A reptile inherits the name, species, and make sound properties/methods from animal
# And has an extra method lay_eggs, and an extra property is_venomous
print(f"{reptile.name}, {reptile.species}, {reptile.is_venomous}, {reptile.make_sound()}, {reptile.lay_eggs()}")

# Private attributes/methods cannot be accessed directly, but can be accessed through public methods

# This works fine, as the private property is accessed through a public method of the Animal class
print(generic_animal.age())

# This should cause an error as the mammal did not inherit the private property age from animal
try:
    print(mammal.age())
except AttributeError as err:
    print("Caught an AttributeError:", err)

# This should cause an error as the dog inherited the faulty method age() from mammal
try:
    print(dog.age())
except AttributeError as err:
    print("Caught an AttributeError:", err)

# This works fine because the Reptile class inherits the public method age() from the Animal class
print(reptile.age())
