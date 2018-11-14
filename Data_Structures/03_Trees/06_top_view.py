# You are given a pointer to the root of a binary tree. Print the top view of the binary tree.


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


def top_view(root):
    # deal with empty tree case
    if root is None:
        return

    # tuple (pos, lvl, node.info)
    tuple_list = [(0, 0, root.info)]
    tuple_append(tuple_list, root.left, 0, 0, 'L')
    tuple_append(tuple_list, root.right, 0, 0, 'R')

    # select tuples with lowest lvl for each pos
    tuple_list.sort(key=lambda tup: (tup[0], tup[1]))
    x = 0
    while x < len(tuple_list) - 1:
        while tuple_list[x][0] == tuple_list[x + 1][0]:
            tuple_list.pop(x + 1)
            if (x + 1) > len(tuple_list) - 1:
                break
        x += 1

    for _, _, data in tuple_list:
        print(data, end=" ")


def tuple_append(ls, node, pos, lvl, direction):
    if node:
        if direction == 'L':
            pos = pos - 1
        elif direction == 'R':
            pos = pos + 1
        lvl = lvl + 1
        ls.append((pos, lvl, node.info))
        tuple_append(ls, node.left, pos, lvl, 'L')
        tuple_append(ls, node.right, pos, lvl, 'R')


tree = BinarySearchTree()
t = int(input())

arr = list(map(int, input().split()))

for i in range(t):
    tree.create(arr[i])

top_view(tree.root)
