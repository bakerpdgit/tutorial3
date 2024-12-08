# Queue class based on a static circular queue implementation
class Queue:
    def __init__(self, maxsize=100): # constructor
        self.__array = [0]*________
        self.__head = -1
        self.__tail = -1
        self.__maxsize = _______
        self.__queue_size = _____

    def is_empty(self): # check if queue is empty
        return self.__queue_size == _________

    def is_full(self): # check if queue is full
        return self.__queue_size == ____________

    def enqueue(self, item): # add an item to the queue
        if ___________():
            raise Exception("Queue full error") 
        self.__tail = (self.__tail + ______) % ___________
        self.__array[self.__tail] = item
        self.__queue_size += ____

    def dequeue(self): # remove and item from the queue
        if self.is_empty():
            raise Exception("Queue empty error")
        self.__head = (_________ + 1) % ________
        self.__queue_size -= ____
        return self.__array[_________]
    
    def __repr__(self): # printing method
        return str(self.__array)

# main part of code
queue = Queue(10)
for i in range(9):
    queue.enqueue(i)
print(queue)
while not queue.is_empty():
    queue.dequeue()
print(queue)
queue.enqueue(11)
queue.enqueue(12)
print(queue)
  
