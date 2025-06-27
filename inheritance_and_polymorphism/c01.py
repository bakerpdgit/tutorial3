class Dog:
    """
        Dog has a speak() method
    """
    def __init__(self, name: str) -> None:
        self.__name = name

    @property
    def name(self) -> str:
        return self.__name

    def speak(self) -> None:
        print("Woof!")

class Cat:
    """
        Cat has a speak() method
    """
    def __init__(self, name: str) -> None:
        self.__name = name

    @property
    def name(self) -> str:
        return self.__name
    
    def speak(self) -> None:
        print("Meow")

class Horse:
    """
        Horse has a speak() method
    """
    def __init__(self, name: str) -> None:
        self.__name = name

    @property
    def name(self) -> str:
        return self.__name

    def speak(self) -> None:
        print("Neigh")

# this will work because Dog, Cat, horse all have a speak() method
# this is an example of polymorphism
animals : list[Dog | Cat | Horse] = [Dog("dog"), Cat("cat"), Horse("horse")]
for animal in animals:
    animal.speak()

