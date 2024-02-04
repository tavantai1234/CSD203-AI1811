class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

def insert_avl(root, key):
    if root is None:
        return AVLNode(key)
    
    if key < root.key:
        root.left = insert_avl(root.left, key)
    else:
        root.right = insert_avl(root.right, key)

    root.height = 1 + max(get_height(root.left), get_height(root.right))

    balance = get_balance(root)

    if balance > 1 and key < root.left.key:
        return rotate_right(root)

    if balance < -1 and key > root.right.key:
        return rotate_left(root)

    if balance > 1 and key > root.left.key:
        root.left = rotate_left(root.left)
        return rotate_right(root)

    if balance < -1 and key < root.right.key:
        root.right = rotate_right(root.right)
        return rotate_left(root)

    return root

def delete_avl(root, key):
    if root is None:
        return root

    if key < root.key:
        root.left = delete_avl(root.left, key)
    elif key > root.key:
        root.right = delete_avl(root.right, key)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        root.key = min_value_node(root.right).key
        root.right = delete_avl(root.right, root.key)

    if root is None:
        return root

    root.height = 1 + max(get_height(root.left), get_height(root.right))

    balance = get_balance(root)

    if balance > 1 and get_balance(root.left) >= 0:
        return rotate_right(root)

    if balance > 1 and get_balance(root.left) < 0:
        root.left = rotate_left(root.left)
        return rotate_right(root)

    if balance < -1 and get_balance(root.right) <= 0:
        return rotate_left(root)

    if balance < -1 and get_balance(root.right) > 0:
        root.right = rotate_right(root.right)
        return rotate_left(root)

    return root

def rotate_right(z):
    y = z.left
    T2 = y.right

    y.right = z
    z.left = T2

    z.height = 1 + max(get_height(z.left), get_height(z.right))
    y.height = 1 + max(get_height(y.left), get_height(y.right))

    return y

def rotate_left(y):
    x = y.right
    T2 = x.left

    x.left = y
    y.right = T2

    y.height = 1 + max(get_height(y.left), get_height(y.right))
    x.height = 1 + max(get_height(x.left), get_height(x.right))

    return x

def get_height(root):
    if root is None:
        return 0
    return root.height

def get_balance(root):
    if root is None:
        return 0
    return get_height(root.left) - get_height(root.right)

def min_value_node(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def preorder_traversal_avl(root):
    if root:
        print(root.key, end=" ")
        preorder_traversal_avl(root.left)
        preorder_traversal_avl(root.right)

def inorder_traversal_avl(root):
    if root:
        inorder_traversal_avl(root.left)
        print(root.key, end=" ")
        inorder_traversal_avl(root.right)

def postorder_traversal_avl(root):
    if root:
        postorder_traversal_avl(root.left)
        postorder_traversal_avl(root.right)
        print(root.key, end=" ")

def level_order_traversal_avl(root):
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
root_avl_1 = None
for key in keys_1:
    root_avl_1 = insert_avl(root_avl_1, key)

print("AVL Tree (1):")
print("Preorder Traversal:", end=" ")
preorder_traversal_avl(root_avl_1)
print("\nInorder Traversal:", end=" ")
inorder_traversal_avl(root_avl_1)
print("\nPostorder Traversal:", end=" ")
postorder_traversal_avl(root_avl_1)
print("\nLevel-order Traversal:", end=" ")
level_order_traversal_avl(root_avl_1)

keys_to_delete_1 = [2, 3, 11]
for key in keys_to_delete_1:
    root_avl_1 = delete_avl(root_avl_1, key)
    print(f"\nAfter deleting {key}:")
    print("Preorder Traversal:", end=" ")
    preorder_traversal_avl(root_avl_1)
    print("\nInorder Traversal:", end=" ")
    inorder_traversal_avl(root_avl_1)
    print("\nPostorder Traversal:", end=" ")
    postorder_traversal_avl(root_avl_1)
    print("\nLevel-order Traversal:", end=" ")
    level_order_traversal_avl(root_avl_1)
    print()

keys_2 = [12, 7, 1, 3, 2, 5, 10, 8, 6, 9]
root_avl_2 = None
for key in keys_2:
    root_avl_2 = insert_avl(root_avl_2, key)

print("\n--------------------------------------------\n")
print("AVL Tree (2):")
print("Preorder Traversal:", end=" ")
preorder_traversal_avl(root_avl_2)
print("\nInorder Traversal:", end=" ")
inorder_traversal_avl(root_avl_2)
print("\nPostorder Traversal:", end=" ")
postorder_traversal_avl(root_avl_2)
print("\nLevel-order Traversal:", end=" ")
level_order_traversal_avl(root_avl_2)

keys_to_delete_2 = [5, 6, 7]
for key in keys_to_delete_2:
    root_avl_2 = delete_avl(root_avl_2, key)
    print(f"\nAfter deleting {key}:")
    print("Preorder Traversal:", end=" ")
    preorder_traversal_avl(root_avl_2)
    print("\nInorder Traversal:", end=" ")
    inorder_traversal_avl(root_avl_2)
    print("\nPostorder Traversal:", end=" ")
    postorder_traversal_avl(root_avl_2)
    print("\nLevel-order Traversal:", end=" ")
    level_order_traversal_avl(root_avl_2)
    print()
