# You’re given the pointer to the head node of a linked list and the position of a node to delete. Delete the node at
# the given position and return the head node. A position of 0 indicates head, a position of 1 indicates one node
# away from the head and so on. The list may become empty after you delete the node.


import os


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node


def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


def delete_node(head, position):
    if head is None:
        return

    temp = head

    if position == 0:
        head = temp.next
        return head

    for i in range(position - 1):
        temp = temp.next
        if temp is None:
            break

    if temp is None:
        return

    if temp.next is None:
        return

    node = temp.next.next
    temp.next = None
    temp.next = node

    return head


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    position = int(input())

    llist1 = delete_node(llist.head, position)

    print_singly_linked_list(llist1, ' ', fptr)
    fptr.write('\n')

    fptr.close()
