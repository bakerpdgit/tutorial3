class Animal:
    """
        Superclass for all the animals
    """
    def __init__(self, name: str) -> None:
        self._name = name

    @property
    def name(self) -> str:
        return self._name

    # for us to use the Animal type annotation for all the subclasses, we must define the speak() method
    # this is a virtual method - it can be overrided later by subclasses
    def speak(self) -> None:
        pass


class Dog(Animal):
    """
        Dog has a speak() method
    """
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def speak(self) -> None:
        print("Woof!")

class Cat(Animal):
    """
        Cat has a speak() method
    """
    def __init__(self, name: str) -> None:
        super().__init__(name)
    
    def speak(self) -> None:
        print("Meow")

class Horse(Animal):
    """
        Horse has a speak() method
    """
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def speak(self) -> None:
        print("Neigh")

# this will work because Dog, Cat, horse all have a speak() method
# this is an example of polymorphism
animals : list[Animal] = [Dog("dog"), Cat("cat"), Horse("horse")]
for animal in animals:
    animal.speak()

