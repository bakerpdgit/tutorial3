from typing import Any


class Stack:
  def __init__(self) -> None:
    self._items: list[Any] = []

  def push(self, item: Any) -> None:
    self._items.append(item)

  def pop(self) -> Any:
    if self.is_empty():
      raise Exception("Stack is empty")
    return self._items.pop()

  def is_empty(self) -> bool:
    return self._items == []

  def peek(self) -> Any:
    return self._items[-1]


words = "man bites dog".split(" ")
my_stack = Stack()

for word in words:
  my_stack.push(word)

while not my_stack.is_empty():
  print(my_stack.pop())
