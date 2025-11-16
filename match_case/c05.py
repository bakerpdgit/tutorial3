match [input("Enter an animal to hear its noise: "), int(input("Enter the number that there are: "))]:
  case ["dog" | "wolf" | "jackal" | "dhole", count]:
    print("Woof " * count)
  case ["cat" | "cheetah" | "ocelot" | "lynx", count]:
    print("Meow " * count)
  case ["monkey" | "bonobo" | "chimp" | "gibbon", count]:
    print("Oo oo aa aa " * count)
  case["horse" | "donkey" | "mule" | "zebra", count]:
    print("Neigh " * count)

match ("Foo", "Bar"):
  case ("Foo", bar) as the_tuple:
    print(bar, the_tuple)

match {"name": "Romeo Montague", "age": 16, "likes": "fighting Capulets"}:
  case {"age": age, "name": name} if age >= 16:
    print(f"{name} is at least 16 years old")
  case _:
    print("This service is only for ages 16 and up")
