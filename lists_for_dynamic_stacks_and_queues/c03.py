from typing import Any


class Queue:
  def __init__(self) -> None:
    self._items: list[Any] = []

  def enqueue(self, item: Any) -> None:
    self._items.append(item)

  def dequeue(self) -> Any:
    if self.is_empty():
      raise Exception("Queue is empty")
    return self._items.pop(0)

  def is_empty(self) -> bool:
    return self._items == []

  def size(self) -> int:
    return len(self._items)


my_queue = Queue()

while True:
  name = input("Enter a name to join the queue or enter when done: ")
  if name == "":
    break
  my_queue.enqueue(name)

print("The queue has", my_queue.size(), "people in it.")
print("Process them in this order: ")

while not my_queue.is_empty():
  print(my_queue.dequeue())

print("The queue is now empty.")
