class PrintableMixin:
    """
        String representation behaviour
    """
    # readable string representation
    def __repr__(self) -> str:
        return f"{self.__class__.__name__}: {self.__dict__}"

# Character is printable
class Character(____________):
    """
        A character has a name and a skin
    """
    def __init__(self, name: str, skin: str) -> None:
        self._name: str = name
        self._skin: str = skin

    @property
    def name(self) -> str:
        return self._name

    @property
    def skin(self) -> str:
        return self._skin

# Movable character inherits from Character
class MovableCharacter(_________, PrintableMixin):
    """
        A character that can move
    """
    def __init__(self, name: str, skin: str) -> None:
        super()._________(name, skin) # call superclass' constructor

    def move(self) -> str:
        return f"{self._name} is moving"

# Attacking character inherits from character
class AttackingCharacter(__________, PrintableMixin):
    """
        A character that can attack
    """
    def __init__(self, name: str, skin: str) -> None:
        _________().__init__(name, skin) # call superclass' constructor

    def attack(self) -> str:
        return f"{self._name} is attacking"

# inherit from MovableCharacter first, then AttackingCharacter
# note that moving attacking character SHOULD NOT inherit from printable mixin
class MovingAttackingCharacter(____________, ____________):
    """
        A character that can move and attack
    """
    def __init__(self, name: str, skin: str) -> None:
        _________._________(name, skin) # call superclass' constructor

# make new moving attacking character
player: MovingAttackingCharacter = MovingAttackingCharacter("Alice", "._.")

# try out its methods and properties
print(player.move())
print(player.attack())
print(player.name, player.skin)

# what do you think this will output?
# this class does not have its own __repr__ method but inherits two different __repr__ methods
print(player)

# prints the method resolution ordering
print(MovingAttackingCharacter.__mro__)

