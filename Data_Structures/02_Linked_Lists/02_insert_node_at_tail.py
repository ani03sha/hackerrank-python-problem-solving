# You are given the pointer to the head node of a linked list and an integer to add to the list. Create a new node
# with the given integer. Insert this node at the tail of the linked list and return the head node of the linked list
#  formed after inserting this new node. The given head pointer may be null, meaning that the initial list is empty.


import os


class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None


def print_singly_linked_list(node, sep, ptr):
    while node:
        ptr.write(str(node.data))

        node = node.next

        if node:
            ptr.write(sep)


def insert_node_at_tail(head, data):
    node = SinglyLinkedListNode(data)

    if head is None:
        head = node
        return head

    n = head

    while n.next:
        n = n.next

    n.next = node

    return head


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    llist_count = int(input())

    llist = SinglyLinkedList()

    for i in range(llist_count):
        llist_item = int(input())
        llist_head = insert_node_at_tail(llist.head, llist_item)
        llist.head = llist_head

    print_singly_linked_list(llist.head, '\n', fptr)
    fptr.write('\n')

    fptr.close()
