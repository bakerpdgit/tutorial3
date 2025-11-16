class Dog:
  def __init__(self, name, size):
    self.name = name
    self.size = size

  def get_sound(self):
    if self.size == 1:
      return "woof"
    elif self.size == 2:
      return "Woof!"
    else:
      return "WOOF!!"

  def growl(self):
    return "Grr"


class Cat:
  def __init__(self, name):
    self.name = name

  def get_sound(self):
    return "Miaou"

  def growl(self):
    return "Grr"

  def pet(self):
    return "Purr purrr"


class Horse:
  def __init__(self, name):
    self.name = name

  def get_sound(self):
    return "Neigh!"

  def growl(self):
    return "Grr"


def make_sound_backwards(animal):
  # Argument can be any animal
  print(animal.get_sound()[::-1])


def call_name(animals, name):
  # `animals` can contain any type of animal or be mixed
  for animal in animals:
    if animal.name == name:
      # Animals called by name should make a reply
      print(animal.get_sound())


make_sound_backwards(Horse("Bill"))
animals = [
    Cat("Tom"), Dog(
        "Spike", 3), Dog(
        "Tyke", 1), Horse("Tom"), Dog(
        "Tom", 2)]
call_name(animals, "Tom")
