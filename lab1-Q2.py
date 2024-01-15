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

    def addToTail(self, x):
        new_node = Node(x)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def addAfter(self, p, x):
        new_node = Node(x)
        current = self.head

        while current:
            if current.data == p:
                new_node.next = current.next
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
        self.head = self.head.next
        return deleted_value

    def deleteFromTail(self):
        if not self.head:
            return None

        if not self.head.next:
            deleted_value = self.head.data
            self.head = None
            return deleted_value

        current = self.head
        while current.next.next:
            current = current.next

        deleted_value = current.next.data
        current.next = None
        return deleted_value

    def deleteAfter(self, p):
        current = self.head

        while current:
            if current.data == p and current.next:
                deleted_value = current.next.data
                current.next = current.next.next
                return deleted_value
            current = current.next

        print(f"Node with value {p} not found or no node after it.")

    def delete(self, x):
        if not self.head:
            return None

        if self.head.data == x:
            deleted_value = self.head.data
            self.head = self.head.next
            return deleted_value

        current = self.head
        while current.next and current.next.data != x:
            current = current.next

        if not current.next:
            print(f"Node with value {x} not found in the list.")
            return None

        deleted_value = current.next.data
        current.next = current.next.next
        return deleted_value

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
    linked_list = SinglyLinkedList()

    linked_list.addToHead(3)
    linked_list.addToHead(7)
    linked_list.addToTail(12)
    linked_list.addAfter(7, 8)

    print("Initial List:")
    linked_list.traverse()

    print("\nDelete from Head:")
    deleted_value_head = linked_list.deleteFromHead()
    print(f"Deleted Value: {deleted_value_head}")
    linked_list.traverse()

    print("\nDelete from Tail:")
    deleted_value_tail = linked_list.deleteFromTail()
    print(f"Deleted Value: {deleted_value_tail}")
    linked_list.traverse()

    print("\nDelete After Node 3:")
    deleted_value_after_3 = linked_list.deleteAfter(3)
    print(f"Deleted Value: {deleted_value_after_3}")
    linked_list.traverse()

    print("\nDelete Node with Value 7:")
    deleted_value_7 = linked_list.delete(7)
    print(f"Deleted Value: {deleted_value_7}")
    linked_list.traverse()

    print("\nSearch for Node with Value 12:")
    node_12 = linked_list.search(12)
    if node_12:
        print(f"Node Found: {node_12.data}")
    
    print("\nNumber of Nodes in the List:", linked_list.count())
