# You’re given the pointer to the head node of a linked list, an integer to add to the list and the position at which
#  the integer must be inserted. Create a new node with the given integer, insert this node at the desired position
# and return the head node.
#
# A position of 0 indicates head, a position of 1 indicates one node away from the head and so on. The head pointer
# given may be null meaning that the initial list is empty.
#
# As an example, if your list starts as 1 -> 2 -> 3 and you want to insert a node at position 2 with data = 4,
# your new list should be 1 -> 2 -> 4 -> 3


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


def insert_node_at_position(head, data, position):
    node = SinglyLinkedListNode(data)
    n = head

    while position > 1:
        n = n.next
        position -= 1

    node.next = n.next
    n.next = node

    return head


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist.insert_node(llist_item)

    data = int(input())

    position = int(input())

    llist_head = insert_node_at_position(llist.head, data, position)

    print_singly_linked_list(llist_head, ' ', fptr)
    fptr.write('\n')

    fptr.close()
