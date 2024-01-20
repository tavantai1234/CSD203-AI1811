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

def real_to_binary(real_number):
    queue = Queue()
    if real_number >= 1 or real_number <= 0:
        raise ValueError("Invalid input. The real number must be less than 1.")

    while real_number > 0:
        real_number *= 2
        bit = int(real_number)
        queue.enqueue(bit)
        real_number -= bit

    binary_representation = ""
    while not queue.isEmpty():
        binary_representation += str(queue.dequeue())

    return binary_representation

if __name__ == "__main__":
    my_queue = Queue()

    my_queue.enqueue(1)
    my_queue.enqueue(2)
    my_queue.enqueue(3)
    my_queue.traverse()

    dequeued_value = my_queue.dequeue()
    print("Dequeued value:", dequeued_value)

    first_value = my_queue.first()
    print("First value:", first_value)

    my_queue.clear()
    print("Queue cleared. Is empty:", my_queue.isEmpty())

    real_number = 0.375
    binary_representation = real_to_binary(real_number)
    print(f"Binary representation of {real_number}: {binary_representation}")
