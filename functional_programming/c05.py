def compose(f, g):
    ...


# Tests
def f(x):
    return 2 * x + 4


def g(x):
    return 3 * x + 3


def capitalise_heads(words):
    for word in words:
        yield word[0].upper() + word[1:]


print(compose(f, g)(42))
# Composing more than two functions in a row takes multiple calls to `compose`, which may be arranged how you wish as
# long as the functions being composed are in the right order
print(compose(compose(" ".join, capitalise_heads), str.split)("when shall we three meet again"))
print(compose(" ".join, compose(capitalise_heads, str.split))("when shall we three meet again"))
