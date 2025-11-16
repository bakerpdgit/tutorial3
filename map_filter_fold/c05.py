from functools import reduce

init = ...


def prepare_predicate(f):
  # prepare_predicate returns a function
  def prepared(a, b):
    ...
  return prepared


def is_large(x):
  return x > 4


def const_false(_):
  return False


print(list(filter(is_large, [1, 7, 2, 6, 8, 2, 3])))
print(reduce(prepare_predicate(is_large), [1, 7, 2, 6, 8, 2, 3], init))

print(list(filter(bool, [True, False, 0, 1, "False", ""])))
print(reduce(prepare_predicate(bool), [True, False, 0, 1, "False", ""], init))

print(list(filter(const_false, [5, 2, 6, 8, 3])))
print(reduce(prepare_predicate(const_false), [5, 2, 6, 8, 3], init))

print(list(filter(is_large, [])))
print(reduce(prepare_predicate(is_large), [], init))
