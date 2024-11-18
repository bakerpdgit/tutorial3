from collections import deque # a double ended queue, more on that later

# Stack class based on a static array implementation
class Stack:
    def __init__(self, maxsize=100):
        self.__array = [0]*______
        self.__top = _____
        self.__maxsize = ________

    def is_empty(self):
        return ____________

    def is_full(self):
        return ________________________
    
    def push(self, item):
        if _____________:
            raise Exception("Stack overflow error")
        self.__top += ____
        self.__array[________] = item

    def pop(self):
        if _____________:
            raise Exception("Stack empty error")
        output = __________[self.__top]
        _________ -= ______
        return output

    def peek(self):
        if ______________:
            raise Exception("stack empty error")
        return self.__array[self.__top]

    def __repr__(self):
        return str(self.__array)

# function to check if the expression is balanced
def is_balanced(expression):
    stack = __________(len(___________))
    for char in expression:
        if char in "({[":
            stack._____(_____)
        elif char in ")}]":
            if stack.______():
                return False
            top_char = stack._____()
            if not __________(top_char, char):
                return False
    return stack.is_empty()

# function to check if opening bracket is the same as the closing bracket
def matches(opening, closing):
    opens = "({["
    closes = ")}]"
    return opens.index(opening) == closes.index(closing)

expression=input()
print(is_balanced(expression))
