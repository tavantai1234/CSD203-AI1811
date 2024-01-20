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

def decimal_to_binary(decimal_number):
    stack = Stack()
    if decimal_number == 0:
        stack.push(0)

    while decimal_number > 0:
        remainder = decimal_number % 2
        stack.push(remainder)
        decimal_number //= 2

    binary_representation = ""
    while not stack.isEmpty():
        binary_representation += str(stack.pop())

    return binary_representation

if __name__ == "__main__":
    my_stack = Stack()
    my_stack.push(1)
    my_stack.push(2)
    my_stack.push(3)
    my_stack.traverse()

    popped_value = my_stack.pop()
    print("Popped value:", popped_value)

    top_value = my_stack.top()
    print("Top value:", top_value)

    my_stack.clear()
    print("Stack cleared. Is empty:", my_stack.isEmpty())

    decimal_number = 15
    binary_representation = decimal_to_binary(decimal_number)
    print(f"Binary representation of {decimal_number}: {binary_representation}")
