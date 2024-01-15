class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addToHead(self, x):
        new_node = Node(x)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def addToTail(self, x):
        new_node = Node(x)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def addAfter(self, p, x):
        new_node = Node(x)
        current = self.head

        while current:
            if current.data == p:
                new_node.prev = current
                new_node.next = current.next
                if current.next:
                    current.next.prev = new_node
                current.next = new_node
                return
            current = current.next

        print(f"Node with value {p} not found in the list.")

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def deleteFromHead(self):
        if not self.head:
            return None

        deleted_value = self.head.data
        if self.head.next:
            self.head.next.prev = None
        self.head = self.head.next

        if not self.head:
            self.tail = None

        return deleted_value

    def deleteFromTail(self):
        if not self.head:
            return None

        deleted_value = self.tail.data
        if self.tail.prev:
            self.tail.prev.next = None
        self.tail = self.tail.prev

        if not self.tail:
            self.head = None

        return deleted_value

    def deleteAfter(self, p):
        current = self.head

        while current:
            if current.data == p and current.next:
                deleted_value = current.next.data
                current.next = current.next.next
                if current.next:
                    current.next.prev = current
                return deleted_value
            current = current.next

        print(f"Node with value {p} not found or no node after it.")

    def delete(self, x):
        current = self.head

        while current:
            if current.data == x:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next

                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev

                return current.data
            current = current.next

        print(f"Node with value {x} not found in the list.")
        return None

    def search(self, x):
        current = self.head

        while current:
            if current.data == x:
                return current
            current = current.next

        print(f"Node with value {x} not found in the list.")
        return None

    def count(self):
        count = 0
        current = self.head

        while current:
            count += 1
            current = current.next

        return count

if __name__ == "__main__":
    doubly_linked_list = DoublyLinkedList()

    doubly_linked_list.addToHead(3)
    doubly_linked_list.addToHead(7)
    doubly_linked_list.addToTail(12)
    doubly_linked_list.addAfter(7, 8)

    print("Initial List:")
    doubly_linked_list.traverse()

    print("\nDelete from Head:")
    deleted_value_head = doubly_linked_list.deleteFromHead()
    print(f"Deleted Value: {deleted_value_head}")
    doubly_linked_list.traverse()

    print("\nDelete from Tail:")
    deleted_value_tail = doubly_linked_list.deleteFromTail()
    print(f"Deleted Value: {deleted_value_tail}")
    doubly_linked_list.traverse()

    print("\nDelete After Node 3:")
    deleted_value_after_3 = doubly_linked_list.deleteAfter(3)
    print(f"Deleted Value: {deleted_value_after_3}")
    doubly_linked_list.traverse()

    print("\nDelete Node with Value 7:")
    deleted_value_7 = doubly_linked_list.delete(7)
    print(f"Deleted Value: {deleted_value_7}")
    doubly_linked_list.traverse()

    print("\nSearch for Node with Value 12:")
    node_12 = doubly_linked_list.search(12)
    if node_12:
        print(f"Node Found: {node_12.data}")

    print("\nNumber of Nodes in the List:", doubly_linked_list.count())
