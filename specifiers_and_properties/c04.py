class Dog:
  """
      Dog class, contains age, name and microchip id
  """

  # constructor
  def __init__(self, name: str, age: int, microchip_id: str):
    self.__age: int = age  # private attribute for age
    self._______: str = _______  # private attribute for name
    self.__microchip_id: str = _______  # private attribute for microchip id

  '''GETTERS'''

  @property
  def age(self) -> int:  # getter for age
    return ________

  @________
  def name(self) -> str:  # getter for name
    return self.__name

  @________
  def microchip_id(self) -> str:  # getter for microchip id
    return self.__microchip_id

  '''SETTERS'''

  @age.setter
  def age(self, value: int) -> None:  # Setter for age with validation
    if value >= 0:
      self.________ = value
    else:
      raise ValueError("Age cannot be negative")

  @name._______
  def name(self, value: str) -> None:  # Setter for name with validation
    if len(value) > 0 and value.isalpha():
      self.________ = value
    else:
      raise ValueError(
          "Name cannot be empty or contain non-alphabetic characters")

  @_____________._______
  def microchip_id(self, value: str) -> None:  # Setter for microchip id
    self.___________ = value


# make new dog
my_dog: Dog = Dog("Panda", 7, "012345678901234")

# get attributes
print(my_dog.name, my_dog.age, my_dog.microchip_id)

my_dog.age += 1  # increase age
my_dog.name = "Pandu"  # change name
my_dog.____________ = "987654321098765"  # change microchip id

# get updated attributes
print(my_dog.__________, my_dog.age, my_dog.microchip_id)
