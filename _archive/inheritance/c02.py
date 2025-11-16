from dataclasses import dataclass


class Animal:
  def __init__(self, name):
    self.name = name

  def growl(self):
    return "Grr"


class Dog(Animal):
  def __init__(self, name, size):
    # Don't worry about this line for now
    super().__init__(name)
    self.size = size

  def get_sound(self):
    if self.size == 1:
      return "woof"
    elif self.size == 2:
      return "Woof!"
    else:
      return "WOOF!!"


class Cat(Animal):
  def get_sound(self):
    return "Miaou"

  def pet(self):
    return "Purr purrr"


class Horse(Animal):
  def get_sound(self):
    return "Neigh!"


@dataclass
class Herd:
  name: str
  # It is possible to write a type which permits multiple different classes - but this solution is wordy and would
  # have to be changed if more animals were introduced
  animals: list[Dog | Cat | Horse]


@dataclass
class Herd2:
  name: str
  # Having one class for all animals allows classes to refer to them directly
  animals: list[Animal]


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
