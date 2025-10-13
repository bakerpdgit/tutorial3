def f(x):
    return 2 * x + 4


def g(x):
    return 3 * x + 3


def f_compose_g(x):
    return f(g(x))


print(f_compose_g(42))


def capitalise_heads(words):
    for word in words:
        yield word[0].upper() + word[1:]


# We can compose multiple functions in a row
# This function could be described as `" ".join ∘ capitalise_heads ∘ str.split`
def title_case(string):
    return " ".join(capitalise_heads(str.split(string)))


print(title_case("hello, world!"))
