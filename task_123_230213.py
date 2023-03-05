class Base:
    def __init__(self, sequence, maximum_number=100):
        self.storage = list(sequence)
        self.maximum_number = maximum_number

    def is_full(self):
        return len(self.storage) == self.maximum_number

    def push(self, element):
        # check it out, this option works exactly the same way and is very interesting
        # if Stack.is_full(self):
        if self.is_full():
            print(f"{self.__class__.__name__} is full")
            return
        self.storage.append(element)

    def is_empty(self):
        return len(self.storage) == 0


class Stack(Base):
    def pop_end(self):
        if Stack.is_empty(self):
            print(f"{self.__class__.__name__} is empty")
            return
        else:
            return self.storage.pop()

    def peek_end(self):
        if Stack.is_empty(self):
            print(f"{self.__class__.__name__} is empty")
            return
        else:
            return self.storage[-1]


class Queue(Base):
    def pop_beginning(self):
        if Stack.is_empty(self):
            print(f"{self.__class__.__name__} is empty")
            return
        else:
            return self.storage.pop(0)


class Deque(Stack, Queue):
    """Deque stands for doubly-ended queue"""
    pass


# # Now let's run some tests

# new_stack = Stack([1, 2, 3, 4,  5], maximum_number=16)
# new_queue = Queue([1, 2, 3, 4,  5], maximum_number=16)
# new_deque = Deque([1, 2, 3, 4,  5], maximum_number=16)

# for item in range(12):
#     new_stack.push(item)
#     new_queue.push(item)
#     new_deque.push(item)

# print()
# print("completed filling items")
# print()

# for item in range(17):
#     new_stack.pop_end()
#     new_queue.pop_beginning()
#     new_deque.pop_beginning()

# print("\n now another test for deque\n")

# for item in range(17):
#     new_deque.push(item)

# for item in range(17):
#     new_deque.pop_end()
