def sum(lst):
    match lst:
        case [head, *tail]:
            return head + sum(tail)
        case []:
            return 0


print(sum([1, 2, 3]))
print(sum([3]))
print(sum([]))


# Returns the result of multiplying all elements together
def product(lst):
    # Your code here
    match ...:
        case [head, *tail]:
            ...
        ...


print(product([1, 2, 3]))
print(product([3]))
print(product([]))


# Reverses a list out-of-place
def reverse(lst):
    # Your code here
    match ...:
        case [head, *tail]:
            ...
        ...


print(reverse([1, 2, 3]))
print(reverse([3]))
print(reverse([]))
