# Queue class based on a static linear queue implementation
class Queue:
    def __init__(self, maxsize=100): # constructor
        self.__array = [0]*maxsize
        self.__head = -1
        self.__tail = -1
        self.__maxsize = maxsize

    def is_empty(self): # check if queue is empty
        return self.__head == self.__tail

    def is_full(self): # check if queue is full
        return self.__tail == self.__maxsize - 1

    def enqueue(self, item): # add an item to the queue
        if self.is_full():
            raise Exception("Queue full error") 
        self.__tail += 1
        self.__array[self.__tail] = item

    def dequeue(self): # remove and item from the queue
        if self.is_empty():
            raise Exception("Queue empty error")
        self.__head += 1
        return self.__array[self.__head]
    
    def __repr__(self): # printing method
        return str(self.__array)

# main part of code
queue = Queue(10)
for i in range(9):
    queue.enqueue(i)
print(queue, queue.is_full())
while not queue.is_empty():
    print(queue.dequeue())

# notice what happens when we print the contents of the queue
print(queue)
queue.enqueue(11)
print(queue)
# this should raise an error, can you find out why?
try:
    queue.enqueue(12)
except Exception as err:
    print(err)
  
