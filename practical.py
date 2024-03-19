class Student:
    def __init__(self, name, age, mark):
        self.name = name
        self.age = age
        self.mark = mark
        self.next = None

class ChainingHashTable:
    def __init__(self):
        self.size = 26
        self.table = [None] * self.size

    def hash_function(self, key):
        index = ord(key[0].lower()) - ord('a')
        return index

    def insert(self, student):
        index = self.hash_function(student.name)
        if self.table[index] is None:
            self.table[index] = student
        else:
            current = self.table[index]
            while current.next is not None:
                current = current.next
            current.next = student

    def display(self):
        for i in range(self.size):
            print(f"Index {i}: ", end="")
            current = self.table[i]
            while current is not None:
                print(f"({current.name}, {current.age}, {current.mark})", end=" -> ")
                current = current.next
            print("None")

hash_table = ChainingHashTable()

hash_table.insert(Student("Alice", 20, 85))
hash_table.insert(Student("Bob", 21, 75))
hash_table.insert(Student("Charlie", 22, 90))
hash_table.insert(Student("David", 19, 95))
hash_table.insert(Student("Emily", 20, 80))

hash_table.display()
