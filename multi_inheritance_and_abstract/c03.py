class _Character:
  """
      A generic character that has a name, skin and coordinates
      This is not supposed to be instantiated
  """

  def __init__(self, name: str, skin: str) -> None:
    self.__name: str = _____
    self.__skin: str = _____
    self.__coords: tuple[int, int] = (0, 0)

  @property
  def name(self) -> str:  # a getter
    return self.__name

  @property
  def skin(self) -> str:  # a getter
    return self.__skin

  @property
  def coords(self) -> tuple[int, int]:  # a getter
    return self.__coords

  @coords._______
  def coords(self, coords: tuple[int, int]) -> None:  # a setter
    self.__coords = coords


class MoveBehaviour:
  """
      Behaviour for a moving character
  """

  def __init__(self, character: _Character) -> None:
    # we store the character so we can use it for calculations
    self.__character: _Character = _________

  """
        This move behaviour increments the x coordinate and decrements the y coordinate
    """

  def move(self) -> str:  # move method
    c = self.__character.coords
    self.__character.________ = (c[0] + 1, c[1] - 1)
    return f"{self.________.name} is moving"


class AttackBehaviour:
  """
      Behaviour for an attacking character
  """

  def __init__(self, character: _Character) -> None:
    self.__character: _Character = ________

  def attack(self) -> str:  # attack method
    return f"{self.__________.name} is attacking"


class Player:
  """
      A wrapper class around a character which is not supposed to be instantiated
  """

  def __init__(self, name: str, skin: str):
    self.__character: _Character = _Character(name, skin)
    self.__mover: MoveBehaviour | None = None
    self.__attacker: AttackBehaviour | None = None

  @property
  def name(self) -> str:
    return self.__character.______

  @property
  def skin(self) -> str:
    return self.__character._______

  @property
  def coords(self) -> tuple[int, int]:
    return self.__character._______

  # we pass in the class so we can instantiate it with the private character
  # attribute
  def setMover(self, mover_cls: type[MoveBehaviour]) -> None:
    self.__mover = _________(self.__character)

  def setAttacker(self, attacker_cls: type[AttackBehaviour]) -> None:
    self.__attacker = _________(self.__character)

  # we forward the internal move method
  def move(self) -> str | None:
    if self.__mover is not None:
      return self.__mover.________()

  # we forward the internal attack method
  def attack(self) -> str | None:
    if self.__attacker is not None:
      return self.__attacker.________()


# we make a player that can move and can attack
# we can make more move behaviours / attack behaviours and this code will
# still be the same
player: Player = Player("Alice", "._.")
player.setMover(MoveBehaviour)
player.setAttacker(AttackBehaviour)

# perform some actions on the player
print(player.coords)
print(player.move())
print(player.attack())
print(player.coords, player.name, player.skin)
