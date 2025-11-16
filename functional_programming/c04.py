def drop_first(lst):
  return lst[1:]


def drop_two(lst):
  return lst[2:]


def drop_last(lst):
  return lst[:-1]


def reverse(lst):
  return lst[::-1]


def del_first_word(string):
  for i in range(len(string)):
    if string[i] == " ":
      return string[i + 1:]
  return ""


def concat(lst):
  return "".join(lst)


def partition(string):
  # If no space is present in the string, returns (string, "", ""). Else, returns (a, " ", c) such that
  # `a + " " + c == string and " " not in a`
  return string.partition(" ")


def delete_last_word(string):
  # If `string` contains no spaces, return ""
  # Else, return the portion of `string` up to and *excluding* the final space
  ...


print("drop_two can be expressed as ___ ∘ ___")
print("drop_last can be expressed as ___ ∘ ___ ∘ ___")
print("del_first_word can be expressed as ___ ∘ ___ ∘ ___ ∘ ___")
