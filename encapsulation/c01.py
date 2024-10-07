class PriorityQueue:
    def __init__(self, size):
        # Entries of the form (value, priority)
        # These are all private attributes
        self.__entries = [(None, None)] * size
        self.__curr_size = 0
        self.__max_size = size

    def create_space(self, priority, start_from):
        """Create space for an entry of the given priority by moving all entries of lesser or equal priority back
        This method should be private because it leaves a hole in the queue which has to be filled by directly
        accessing self.__entries"""
        if start_from == self.__max_size:
            raise RuntimeError("Queue full")
        i = start_from
        while i > 0:
            _, check = self.__entries[i - 1]
            if check <= priority:
                self.__entries[i] = self.__entries[i - 1]
                i -= 1
            else:
                break
        return i
    
    def add(self, value, priority):
        insertion_position = self.create_space(priority, self.__curr_size)
        self.__entries[insertion_position] = (value, priority)
        self.__curr_size += 1
    
    def increase_priority(self, value, new_priority):
        for i, (check, _) in enumerate(self.__entries[:self.__curr_size]):
            if check == value:
                index = i
                break
        else:
            raise ValueError(f"{value} is not in the queue")
        _, old_priority = self.__entries[index]
        if old_priority >= new_priority:
            raise ValueError(f"Priority must be increased")
        insertion_position = self.create_space(new_priority, index)
        self.__entries[insertion_position] = value, new_priority
    
    def pop(self):
        result = self.__entries[0][0]
        for i in range(1, self.__curr_size):
            self.__entries[i-1] = self.__entries[i]
        self.__curr_size -= 1
        return result


# Normal use of a queue
queue = PriorityQueue(5)
queue.add("Wash dishes", 3)
queue.add("Do laundry", 1)
queue.add("Put bins out", 4)
print(queue.pop())
queue.add("Go shopping", 2)
queue.increase_priority("Do laundry", 5)
print(queue.pop())

# Dangerous code
queue.create_space(3, 2)
# Washing dishes has been duplicated - unintended behaviour
print(queue.pop())
print(queue.pop())
# This raises an unexpected error which could be hard to debug
queue.create_space(2, 4)
