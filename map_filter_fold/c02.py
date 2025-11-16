from functools import reduce


# we will not give type annotations for these as it is a bit more complicated
def add(a, b):
  return a + b


def multiply(a, b):
  return a * b


nums = [2, 3, 5, 7, 11, 13]

# Alternatively: reduce(add, nums)
sum = reduce(add, nums, 0)
print(sum)

# Alternatively: reduce(multiply, nums, 1)
product = reduce(multiply, nums)
print(product)
