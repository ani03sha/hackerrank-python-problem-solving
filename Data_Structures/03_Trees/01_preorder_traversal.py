# Print the tree's preorder traversal as a single line of space-separated values.


class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


def pre_order(root):
    if root is None:
        return

    print(root.info, end=' ')
    pre_order(root.left)
    pre_order(root.right)


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

pre_order(tree.root)
