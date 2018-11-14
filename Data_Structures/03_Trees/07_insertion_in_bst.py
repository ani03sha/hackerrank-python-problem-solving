# You are given a pointer to the root of a binary search tree and values to be inserted into the tree. Insert the
# values into their appropriate position in the binary search tree and return the root of the updated binary tree.
# You just have to complete the function.


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


def preOrder(root):
    if root is None:
        return
    print(root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)


class BinarySearchTree:
    def __init__(self):
        self.root = None


def insert(self, val):
    if self is None:
        self = Node(val)
    elif self.info > val:
        self.left = insert(self.left, val)
    elif self.info < val:
        self.right = insert(self.right, val)
    return self


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    insert(None, arr[i])

preOrder(tree.root)
