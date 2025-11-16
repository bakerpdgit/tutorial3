city = input("Enter a city: ")
if city == "Jakarta":
  print("06°10′S 106°49′E")
elif city == "Phnom Penh":
  print("11°34′N 104°55′E")
elif city == "Shanghai":
  print("31°13′N 121°28′E")
elif city == "Cairo":
  print("30°2′N 31°14′E")
elif city == "Lagos":
  print("06°27′N 03°23′E")
else:
  print(f"I don't know where {city} is")


number = input("Enter your favourite number: ")
if number == "0":
  print("That's my favourite too!")
elif number == "1":
  print("All alone...")
elif number == "2":
  print("The only even prime!")
elif number == "3":
  print("The only prime that's a multiple of three...")
else:
  print("Too big!")


x, y = int(input("Enter two numbers: ")), int(input("... "))
operator = input("Enter an operator: ")
if operator == "+":
  print(x + y)
elif operator == "*":
  print(x * y)
elif operator == "-":
  print(x - y)
elif operator == "/":
  print(x / y)
