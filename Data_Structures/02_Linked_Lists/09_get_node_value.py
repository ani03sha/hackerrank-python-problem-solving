# You’re given the pointer to the head node of a linked list and a specific position. Counting backwards from the
# tail node of the linked list, get the value of the node at the given position. A position of 0 corresponds to the
# tail, 1 corresponds to the node before the tail and so on.


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


def get_node(head, positionFromTail):

    if head is None:
        return

    count = 0
    main = head
    reference = head

    while count <= positionFromTail:
        reference = reference.next
        count += 1

    while reference is not None:
        main = main.next
        reference = reference.next

    return main.data



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        position = int(input())

        result = get_node(llist.head, position)

        fptr.write(str(result) + '\n')

    fptr.close()


