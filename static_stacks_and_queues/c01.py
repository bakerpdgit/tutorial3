# Stack class based on a static array implementation
class Stack:
    def __init__(self, maxsize=100):
        self.__array = [0]*maxsize
        self.__top = -1
        self.__maxsize = maxsize

    def is_empty(self):
        return self.__top == -1

    def is_full(self):
        return self.__top == self.__maxsize - 1
    
    def push(self, item):
        if self.is_full():
            raise Exception("Stack overflow error")
        self.__top += 1
        self.__array[self.__top] = item

    def pop(self):
        if self.is_empty():
            raise Exception("Stack empty error")
        output = self.__array[self.__top]
        self.__top -= 1
        return output

    def peek(self):
        if self.is_empty():
            raise Exception("stack empty error")
        return self.__array[self.__top]

    def __repr__(self):
        return str(self.__array)

stack = Stack(3)
stack.push(5) # the stack is now [5]
stack.push(4) # the stack is now [5, 4]
stack.push(3) # the stack is now [5, 4, 3]
print(stack.is_full(), stack.is_empty()) # True, False
try:
    stack.push(2) # should raise an error
except Exception as err:
    print(err)
print(stack.peek()) # returns 3
print(stack.pop()) # the stack is now [5, 4], returns 3
print(stack.peek()) # returns 4
print(stack.pop()) # the stack is now [5], returns 4
print(stack.is_full(), stack.is_empty()) # False, False
print(stack.pop()) # the stack is now empty, returns 5
print(stack.is_full(), stack.is_empty()) # False, True
try:
    stack.pop() # should raise an error
except Exception as err:
    print(err)
