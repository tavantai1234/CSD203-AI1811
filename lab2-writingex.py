#1)
x = 3
y = 5
z = 2

s.makeEmpty()  

s.push(x)      
s.push(4)     
s.pop()        

s.push(y)      
s.push(3)      
s.push(z)      

s.pop()        
s.push(2)      
s.push(x)      

while not s.isEmpty():
    print('s.pop() ', s.pop(), " ")

#2) 
x = 3
y = 1

s.makeEmpty()  

s.push(5)      
s.push(7)      
s.pop()        
x += y         

s.pop()        

s.push(x)      
s.push(y)     
s.push(2)     
s.pop()       
s.pop()        

while not s.isEmpty():
    y = s.pop()
    print(y)

print('x =', x)  
print('y =', y) 

#3)
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop()

    def isEmpty(self):
        return len(self.items) == 0

def process_sequence(sequence):
    stack = Stack()
    result_values = []

    for operation in sequence:
        if operation.isalpha():  
            stack.push(operation)
        elif operation == '*':    
            popped_value = stack.pop()
            if popped_value is not None:
                result_values.append(popped_value)

    return result_values

sequence = "EAS*Y*QUE***ST***ION***"
result_values = process_sequence(sequence)

print("Sequence of values:", result_values)

#4)

def process_sequence(sequence):
    s = [] 
    result_contents = []
    for operation in sequence:
        if operation.isalpha():  
            s.append(operation)
        elif operation == '*':   
            if s:
                popped_value = s.pop()
                result_contents.append(popped_value)
    return result_contents

sequence = "LA*STI*N*FIR*ST**OU*T*****"
result_contents = process_sequence(sequence)[:5]

print("Contents:", result_contents)

#5) 
from collections import deque

def process_sequence(sequence):
    queue = deque()  
    result_values = []

    for operation in sequence:
        if operation.isalpha(): 
            queue.append(operation)
        elif operation == '*':    
            if queue:
                dequeued_value = queue.popleft()
                result_values.append(dequeued_value)

    return result_values

sequence = "EAS*Y*QUE***ST***ION***"
result_values = process_sequence(sequence)

print("Sequence:", result_values)

#6)
class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.q = [None] * size
        self.front = self.rear = -1

    def enqueue(self, item):
        if (self.rear + 1) % self.size == self.front:
            print("Queue is full, Cannot enqueue", item)
        elif self.isEmpty():
            self.front = self.rear = 0
            self.q[self.rear] = item
        else:
            self.rear = (self.rear + 1) % self.size
            self.q[self.rear] = item

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty, Cannot dequeue.")
        elif self.front == self.rear:
            dequeued_value = self.q[self.front]
            self.front = self.rear = -1
            return dequeued_value
        else:
            dequeued_value = self.q[self.front]
            self.front = (self.front + 1) % self.size
            return dequeued_value

    def isEmpty(self):
        return self.front == -1

sequence = "EAS*Y*QUE***ST***ION***"
cq = CircularQueue(size=5)

for operation in sequence:
    if operation.isalpha():  
        cq.enqueue(operation)
    elif operation == '*':
        cq.dequeue()

result_contents = [cq.q[i] for i in range(5)]

print("Contents:", result_contents)
