# You’re given the pointer to the head node of a linked list and an integer to add to the list. Create a new node
# with the given integer, insert this node at the head of the linked list and return the new head node. The head
# pointer given may be null meaning that the initial list is empty.


import os

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


def insert_node_at_head(llist, data):
    node = SinglyLinkedListNode(data)
    node.next = llist
    head = llist
    return head


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for _ in range(llist_count):
        llist_item = int(input())
        llist_head = insert_node_at_head(llist.head, llist_item)
        llist.head = llist_head

    print_singly_linked_list(llist.head, '\n', fptr)
    fptr.write('\n')

    fptr.close()
