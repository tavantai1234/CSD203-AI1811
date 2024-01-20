class EmptyStackException(Exception):
    pass

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

def decimal_to_binary(decimal_number):
    stack = Stack()

    if decimal_number == 0:
        stack.push('0')

    while decimal_number > 0:
        remainder = decimal_number % 2
        stack.push(chr(ord('0') + remainder))
        decimal_number //= 2

    binary_representation = ""
    while not stack.isEmpty():
        binary_representation += stack.pop()

    return binary_representation

def real_to_binary(real_number):
    queue = Queue()

    if not (0 < real_number < 1):
        raise ValueError("Invalid input. The real number must be between 0 and 1 exclusive.")

    while real_number > 0:
        real_number *= 2
        bit = int(real_number)
        queue.enqueue(chr(ord('0') + bit))
        real_number -= bit

    binary_representation = ""
    while not queue.isEmpty():
        binary_representation += queue.dequeue()

    return binary_representation

def main():
    my_stack = Stack()
    my_stack.push('A')
    my_stack.push('B')
    my_stack.push('C')
    my_stack.traverse()

    popped_value = my_stack.pop()
    print("Popped value:", popped_value)

    top_value = my_stack.top()
    print("Top value:", top_value)

    my_stack.clear()
    print("Stack cleared. Is empty:", my_stack.isEmpty())

    my_queue = Queue()
    my_queue.enqueue('X')
    my_queue.enqueue('Y')
    my_queue.enqueue('Z')
    my_queue.traverse()

    dequeued_value = my_queue.dequeue()
    print("Dequeued value:", dequeued_value)

    first_value = my_queue.first()
    print("First value:", first_value)

    my_queue.clear()
    print("Queue cleared. Is empty:", my_queue.isEmpty())

    decimal_number = 15
    binary_representation = decimal_to_binary(decimal_number)
    print(f"Binary representation of {decimal_number}: {binary_representation}")

    real_number = 0.375
    binary_representation = real_to_binary(real_number)
    print(f"Binary representation of {real_number}: {binary_representation}")

if __name__ == "__main__":
    main()
