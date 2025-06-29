class Character:
    """
        A character has a name and a skin
    """
    def __init__(self, name: str, skin: str):
        self.__name: str = name
        self.__skin: str = skin

    @property
    def name(self) -> str:
        return self.__name

    @property
    def skin(self) -> str:
        return self.__skin

class Movable:
    """
        Move behaviour mixin
    """
    def move(self):
        return f"{self.name} is moving"

class Attackable:
    """
        Attack behaviour mixin
    """
    def attack(self):
        return f"{self.name} is attacking"

class Player(Character, Movable, Attackable):
    """
        A player is a character that can move and can attack
    """
    pass

player: Player = Player("Alice", "._.")
print(player.move())
print(player.attack())


