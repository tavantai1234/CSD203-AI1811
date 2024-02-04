class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if key < root.key:
            root.left = insert(root.left, key)
        else:
            root.right = insert(root.right, key)
    return root

def delete(root, key):
    if root is None:
        return root

    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        root.key = min_value_node(root.right).key
        root.right = delete(root.right, root.key)

    return root

def min_value_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def preorder_traversal(root):
    if root:
        print(root.key, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)

def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.key, end=" ")
        inorder_traversal(root.right)

def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.key, end=" ")

def level_order_traversal(root):
    if not root:
        return

    queue = [root]
    while queue:
        node = queue.pop(0)
        print(node.key, end=" ")

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

keys_1 = [4, 3, 1, 11, 5, 9, 2, 6, 15, 12]
root_1 = None
for key in keys_1:
    root_1 = insert(root_1, key)

print("Before Deletions:")
print("Preorder Traversal:", end=" ")
preorder_traversal(root_1)
print("\nInorder Traversal:", end=" ")
inorder_traversal(root_1)
print("\nPostorder Traversal:", end=" ")
postorder_traversal(root_1)
print("\nLevel-order Traversal:", end=" ")
level_order_traversal(root_1)

keys_to_delete_1 = [2, 3, 11]
for key in keys_to_delete_1:
    root_1 = delete(root_1, key)
    print(f"\nAfter deleting {key}:")
    print("Preorder Traversal:", end=" ")
    preorder_traversal(root_1)
    print("\nInorder Traversal:", end=" ")
    inorder_traversal(root_1)
    print("\nPostorder Traversal:", end=" ")
    postorder_traversal(root_1)
    print("\nLevel-order Traversal:", end=" ")
    level_order_traversal(root_1)
    print()

keys_2 = [12, 7, 1, 3, 2, 5, 10, 8, 6, 9]
root_2 = None
for key in keys_2:
    root_2 = insert(root_2, key)

print("\n--------------------------------------------\n")
print("Before Deletions:")
print("Preorder Traversal:", end=" ")
preorder_traversal(root_2)
print("\nInorder Traversal:", end=" ")
inorder_traversal(root_2)
print("\nPostorder Traversal:", end=" ")
postorder_traversal(root_2)
print("\nLevel-order Traversal:", end=" ")
level_order_traversal(root_2)

keys_to_delete_2 = [5, 6, 7]
for key in keys_to_delete_2:
    root_2 = delete(root_2, key)
    print(f"\nAfter deleting {key}:")
    print("Preorder Traversal:", end=" ")
    preorder_traversal(root_2)
    print("\nInorder Traversal:", end=" ")
    inorder_traversal(root_2)
    print("\nPostorder Traversal:", end=" ")
    postorder_traversal(root_2)
    print("\nLevel-order Traversal:", end=" ")
    level_order_traversal(root_2)
    print()
