from abc import ABC, abstractmethod


class Player(ABC):
    '''Player class (abstract class)'''

    def __init__(self, name: str) -> None:  # Constructor
        super().__init__()  # Call the constructor of the ABC parent class
        self._name: str = name
        self._position: tuple[float, float] = (0, 0)

    @property
    def position(self) -> tuple[float, float]:
        return self._position

    # ABSTRACT METHOD, must be implemented for class to be instantiated
    @abstractmethod
    def attack(self) -> None:
        pass

    def move(self) -> None:  # VIRTUAL METHOD, has an implementation but is overriden later
        self._position = (self._position[0] + 1, self._position[1] + 1)

    def __repr__(self) -> str:  # Printing method
        return f"{self._name} is at position {self._position}"


class Warrior(Player):
    '''Warrior class inherits from Player class'''

    def __init__(self, name: str) -> None:  # Constructor
        super().__init__(name)

    def move(self) -> None:  # Override virtual method
        self._position = (self._position[0] + 2, self._position[1] + 2)

    def attack(self) -> None:  # Override the abstract method
        print(f"Warrior {self._name} is attacking with a sword.")


class Mage(Player):
    '''Mage class inherits from Player class'''

    def __init__(self, name : str) -> None:  # Constructor
        super().__init__(name)

    def move(self) -> None:  # Override virtual method
        self._position = (self._position[0] + 0.5, self._position[1] + 0.5)

    def attack(self) -> None:  # Override the abstract method
        print(f"Mage {self._name} is casting a fireball.")


# Try to instantiate abstract class Player
try:
    print("This next line should trigger an error ...")
    player: Player = Player("(^ω^)")
except Exception as err:
    print(f"Error caught: {err}")

# Create instances of the classes
warrior: Warrior = Warrior("(^ω^)")
mage: Mage = Mage("(●´ω｀●)")

# Attack method (abstract method but overriden)
warrior.attack()
mage.attack()

# Move method (virtual method but overriden)
warrior.move()
mage.move()
print(warrior.position, mage.position)
