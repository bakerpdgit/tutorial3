class Animal:
  """
      Superclass for all the animals
  """

  def __init__(self, name: str) -> None:
    self._name = name  # protected attribute

  @property
  def name(self) -> str:
    return self._name

  # to use the type annotations, we must define the speak() method here
  # it will still run without, but it is best to define it
  # this is a virtual method
  def speak(self) -> None:
    pass


class Dog(Animal):
  """
      Dog has a speak() method
  """

  def __init__(self, name: str) -> None:
    super().__init__(name)  # superconstructor

  def speak(self) -> None:  # method overriding
    print("Woof!")


class Cat(Animal):
  """
      Cat has a speak() method
  """

  def __init__(self, name: str) -> None:
    super().__init__(name)  # superconstructor

  def speak(self) -> None:  # method overriding
    print("Meow")


class Horse(Animal):
  """
      Horse has a speak() method
  """

  def __init__(self, name: str) -> None:
    super().__init__(name)  # superconstructor

  def speak(self) -> None:  # method overriding
    print("Neigh")

  def dosomething(self) -> None:
    print("hey hey hey")


# this will work because Dog, Cat, horse all have a speak() method
# this is an example of polymorphism
animals: list[Animal] = [Dog("dog"), Cat("cat"), Horse("horse")]
for animal in animals:
  animal.speak()
