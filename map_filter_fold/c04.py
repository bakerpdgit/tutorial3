def is_title_case(s: str) -> bool:
    return all(word[0].isupper() for word in s.split(" "))


plays = ["Romeo and Juliet", "As You Like It", "Macbeth", "cymbeline"]

# No conversion required
for play in filter(is_title_case, plays):
    print(play)

# Prints "filter object"
print(filter(is_title_case, plays))

# Prints a list
print(list(filter(is_title_case, plays)))
