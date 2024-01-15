class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def addToHead(self, x):
        new_node = Node(x)
        new_node.next = self.head
        self.head = new_node

    def displayList(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

if __name__ == "__main__":
    linked_list = SinglyLinkedList()

    linked_list.addToHead(3)
    linked_list.addToHead(7)
    linked_list.addToHead(12)

    linked_list.displayList()