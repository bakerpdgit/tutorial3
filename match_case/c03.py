from dataclasses import dataclass

# Case statements can be tuples with a mixture of literals and identifiers
value = ("cat", "meow")  # Change this to experiment
match value:
  case "cat", "meow":
    print("Cats are most commonly thought to say meow")
  case "cat", sound:
    print(f"Cats make all sorts of funny sounds, including {sound}")
  case animal, "bark":
    print(f"Even a {animal} can bark if it tries hard enough")
  # Case statement syntax looks a lot like assignment syntax. For instance, this case looks like the assignment
  # `animal, sound = value`
  case animal, sound:
    print(f"{animal} makes the sound {sound}")
  case _:
    print("Malformed data; please use a tuple of two elements")

# You can also use * in case statements as in assignments:
animals = ["lion", "monkey", "crocodile", "bird", "leopard"]
match animals:
  case [first, *rest]:
    print(
        f"The {first} is king of the jungle, in charge of the other animals: {', '.join(rest)}")
  case []:
    print("There are no animals left!")

match [1, 2, 3, 5, 8, 13]:
  # You can have literals and identifiers before and after a starred identifier, but only up to one starred
  # identifier per list since multiple would be ambiguous
  case [a, *nums, 8, c]:
    print(a, nums, c)

# You can match on a dictionary, extracting some of its values by key name...
characters = {
    "name": "Romeo Montague",
    "age": 16,
    "likes": "fighting Capulets"}

match characters:
  case {"age": 16, "name": name}:
    print(f"{name} is 16 years old")
  case _:
    print("This service is only for 16-year-olds")

# ... and optionally getting the remaining values through double-starred identifiers like in parameter lists
words = {"foo": "bar", "knights": "ni", "fresh": "fruit"}
match words:
  case {"foo": _, **rest}:
    print(rest)


# You can even use match statements on classes, matching by their attributes. Note we match by attribute name, not
# by constructor parameters
class Parrot:
  def __init__(self, plumage_, beak):
    self.plumage = plumage_
    self.beak = beak


my_parrot = Parrot("green", "red")
match my_parrot:
  case Parrot(plumage=plumage):
    print(f"The parrot has {plumage} plumage")
  case _:
    print("That isn't a parrot...")


@dataclass
class Macaw:
  plumage: str
  beak: str


# For dataclasses, you can also match attributes positionally
my_macaw = Macaw("blue and gold", "black")
match my_macaw:
  case Macaw("blue and gold", beak):
    print(
        f"The blue-and-gold macaw is blue on the top and yellow on the bottom with a {beak} beak")
  case Macaw(plumage, beak):
    print(f"The macaw has {plumage} plumage and a {beak} beak")


# All of these patterns can be nested
animal_collection = {
    "parrots": [Parrot("green", "red"), Macaw("blue", "black")],
    "puffins": [],
    "owls": []
}
match animal_collection:
  case {"parrots": [Parrot(beak=red), *other_parrots], **other_birds}:
    print(other_parrots, other_birds)
  case _:
    print("The first parrot didn't have a red beak")
