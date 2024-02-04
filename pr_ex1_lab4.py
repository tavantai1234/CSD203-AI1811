class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def isEmpty(self):
        return self.root is None

    def clear(self):
        self.root = None

    def search(self, x):
        return self._search(self.root, x)

    def _search(self, root, x):
        if root is None or root.key == x:
            return root
        if x < root.key:
            return self._search(root.left, x)
        return self._search(root.right, x)

    def insert(self, x):
        self.root = self._insert(self.root, x)

    def _insert(self, root, x):
        if root is None:
            return TreeNode(x)
        if x < root.key:
            root.left = self._insert(root.left, x)
        elif x > root.key:
            root.right = self._insert(root.right, x)
        return root

    def breadth(self):
        if self.root is None:
            return []

        result = []
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            result.append(node.key)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

    def preorder(self):
        return self._preorder(self.root)

    def _preorder(self, root):
        if root is None:
            return []
        return [root.key] + self._preorder(root.left) + self._preorder(root.right)

    def inorder(self):
        return self._inorder(self.root)

    def _inorder(self, root):
        if root is None:
            return []
        return self._inorder(root.left) + [root.key] + self._inorder(root.right)

    def postorder(self):
        return self._postorder(self.root)

    def _postorder(self, root):
        if root is None:
            return []
        return self._postorder(root.left) + self._postorder(root.right) + [root.key]

    def count(self):
        return self._count(self.root)

    def _count(self, root):
        if root is None:
            return 0
        return 1 + self._count(root.left) + self._count(root.right)

    def dele(self, x):
        self.root = self._dele(self.root, x)

    def _dele(self, root, x):
        if root is None:
            return root
        if x < root.key:
            root.left = self._dele(root.left, x)
        elif x > root.key:
            root.right = self._dele(root.right, x)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.key = self._min_value_node(root.right).key
            root.right = self._dele(root.right, root.key)
        return root

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def min(self):
        return self._min(self.root)

    def _min(self, root):
        if root is None:
            return None
        while root.left is not None:
            root = root.left
        return root.key

    def max(self):
        return self._max(self.root)

    def _max(self, root):
        if root is None:
            return None
        while root.right is not None:
            root = root.right
        return root.key

    def _sum(self, root):
        if root is None:
            return 0
        return root.key + self._sum(root.left) + self._sum(root.right)

    def sum(self):
        return self._sum(self.root)

    def avg(self):
        count = self.count()
        if count == 0:
            return 0
        return self.sum() / count

    def height(self):
        return self._height(self.root)

    def _height(self, root):
        if root is None:
            return 0
        return 1 + max(self._height(root.left), self._height(root.right))

    def cost_of_most_expensive_path(self):
        return self._cost_of_most_expensive_path(self.root)

    def _cost_of_most_expensive_path(self, root):
        if root is None:
            return 0
        return root.key + max(
            self._cost_of_most_expensive_path(root.left),
            self._cost_of_most_expensive_path(root.right)
        )

    def is_avl(self):
        return self._is_avl(self.root)

    def _is_avl(self, root):
        if root is None:
            return True

        left_height = self._height(root.left)
        right_height = self._height(root.right)

        if abs(left_height - right_height) > 1:
            return False

        return self._is_avl(root.left) and self._is_avl(root.right)

    def is_heap(self):
        return self._is_heap(self.root)

    def _is_heap(self, root):
        if root is None:
            return True

        if root.left and root.left.key > root.key:
            return False
        if root.right and root.right.key > root.key:
            return False

        return self._is_heap(root.left) and self._is_heap(root.right)

bst = BinarySearchTree()
bst.insert(8)
bst.insert(3)
bst.insert(10)
bst.insert(1)
bst.insert(6)
bst.insert(14)
bst.insert(4)
bst.insert(7)
bst.insert(13)

print("Breadth Traversal:", bst.breadth())
print("Preorder Traversal:", bst.preorder())
print("Inorder Traversal:", bst.inorder())
print("Postorder Traversal:", bst.postorder())
print("Number of Nodes:", bst.count())
print("Sum of Values:", bst.sum())
print("Average of Values:", bst.avg())
print("Height of Tree:", bst.height())
print("Cost of Most Expensive Path:", bst.cost_of_most_expensive_path())
print("Is AVL Tree:", bst.is_avl())
print("Is Heap:", bst.is_heap())
