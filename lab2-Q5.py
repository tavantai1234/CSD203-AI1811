class EmptyStackException(Exception):
    pass

class Computer:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def clear(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def pop(self):
        if self.isEmpty():
            raise EmptyStackException("Stack is empty")
        return self.items.pop()

    def top(self):
        if self.isEmpty():
            raise EmptyStackException("Stack is empty")
        return self.items[-1]

    def traverse(self):
        print("Stack contents from top to bottom:")
        for item in reversed(self.items):
            print(item)

class EmptyQueueException(Exception):
    pass

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return len(self.items) == 0

    def clear(self):
        self.items = []

    def enqueue(self, x):
        self.items.append(x)

    def dequeue(self):
        if self.isEmpty():
            raise EmptyQueueException("Queue is empty")
        return self.items.pop(0)

    def first(self):
        if self.isEmpty():
            raise EmptyQueueException("Queue is empty")
        return self.items[0]

    def traverse(self):
        print("Queue contents from front to rear:")
        for item in self.items:
            print(item)

def main():
    my_stack = Stack()
    my_stack.push(Computer("Desktop1"))
    my_stack.push(Computer("Laptop2"))
    my_stack.push(Computer("Server3"))
    my_stack.traverse()

    popped_value = my_stack.pop()
    print("Popped value:", popped_value)

    top_value = my_stack.top()
    print("Top value:", top_value)

    my_stack.clear()
    print("Stack cleared. Is empty:", my_stack.isEmpty())

    my_queue = Queue()
    my_queue.enqueue(Computer("WorkstationA"))
    my_queue.enqueue(Computer("ServerB"))
    my_queue.enqueue(Computer("LaptopC"))
    my_queue.traverse()

    dequeued_value = my_queue.dequeue()
    print("Dequeued value:", dequeued_value)

    first_value = my_queue.first()
    print("First value:", first_value)

    my_queue.clear()
    print("Queue cleared. Is empty:", my_queue.isEmpty())

if __name__ == "__main__":
    main()
