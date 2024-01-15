class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def addToHead(self, x):
        new_node = Node(x)
        if not self.head:
            new_node.next = new_node  
            self.head = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            new_node.next = self.head
            current.next = new_node
            self.head = new_node

    def addToTail(self, x):
        new_node = Node(x)
        if not self.head:
            new_node.next = new_node 
            self.head = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            new_node.next = self.head
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
            if current == self.head:
                break  

        print(f"Node with value {p} not found in the list.")

    def traverse(self):
        if not self.head:
            return

        current = self.head
        while True:
            print(current.data, end=" ")
            current = current.next
            if current == self.head:
                break 

        print()

    def deleteFromHead(self):
        if not self.head:
            return None

        deleted_value = self.head.data

        if self.head.next == self.head:
            self.head = None
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next

        return deleted_value

    def deleteFromTail(self):
        if not self.head:
            return None

        deleted_value = self.head.data

        if self.head.next == self.head:
            self.head = None
        else:
            current = self.head
            while current.next.next != self.head:
                current = current.next
            current.next = self.head

        return deleted_value

    def deleteAfter(self, p):
        if not self.head:
            return None

        current = self.head
        while current:
            if current.data == p and current.next != self.head:
                deleted_value = current.next.data
                current.next = current.next.next
                return deleted_value
            current = current.next
            if current == self.head:
                break  

        print(f"Node with value {p} not found or no node after it.")
        return None

    def delete(self, x):
        if not self.head:
            return None

        if self.head.data == x:
            return self.deleteFromHead()

        current = self.head
        while current.next != self.head and current.next.data != x:
            current = current.next

        if current.next == self.head:
            print(f"Node with value {x} not found in the list.")
            return None

        deleted_value = current.next.data
        current.next = current.next.next
        return deleted_value

    def search(self, x):
        if not self.head:
            print(f"Node with value {x} not found in the list.")
            return None

        current = self.head
        while current:
            if current.data == x:
                return current
            current = current.next
            if current == self.head:
                break  

        print(f"Node with value {x} not found in the list.")
        return None

    def count(self):
        count = 0
        current = self.head

        if not current:
            return count

        while True:
            count += 1
            current = current.next
            if current == self.head:
                break 

        return count

if __name__ == "__main__":
    circular_linked_list = CircularLinkedList()

    circular_linked_list.addToHead(3)
    circular_linked_list.addToHead(7)
    circular_linked_list.addToTail(12)
    circular_linked_list.addAfter(7, 8)

    print("Initial List:")
    circular_linked_list.traverse()

    print("\nDelete from Head:")
    deleted_value_head = circular_linked_list.deleteFromHead()
    print(f"Deleted Value: {deleted_value_head}")
    circular_linked_list.traverse()

    print("\nDelete from Tail:")
    deleted_value_tail = circular_linked_list.deleteFromTail()
    print(f"Deleted Value: {deleted_value_tail}")
    circular_linked_list.traverse()

    print("\nDelete After Node 3:")
    deleted_value_after_3 = circular_linked_list.deleteAfter(3)
    print(f"Deleted Value: {deleted_value_after_3}")
    circular_linked_list.traverse()

    print("\nDelete Node with Value 7:")
    deleted_value_7 = circular_linked_list.delete(7)
    print(f"Deleted Value: {deleted_value_7}")
    circular_linked_list.traverse()

    print("\nSearch for Node with Value 12:")
    node_12 = circular_linked_list.search(12)
    if node_12:
        print(f"Node Found: {node_12.data}")

    print("\nNumber of Nodes in the List:", circular_linked_list.count())
