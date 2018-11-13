# Given a reference to the head of a doubly-linked list and an integer, data, create a new DoublyLinkedListNode
# object having data value data and insert it into a sorted linked list while maintaining the sort.


import os


class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail

        self.tail = node


def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)


def sorted_insert(head, data):
    n = DoublyLinkedListNode(data)
    current = head

    if head is None:
        return n

    while current is not None:
        if current.data > data:
            n.next = current
            n.prev = current.prev
            current.prev = n

            if n.prev is None:
                return n
            else:
                n.prev.next = n
                return head

        if current.next is None:
            n.prev = current
            n.next = None
            current.next = n
            break

        current = current.next

    return head


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        llist_count = int(input())

        llist = DoublyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        data = int(input())

        llist1 = sorted_insert(llist.head, data)

        print_doubly_linked_list(llist1, ' ', fptr)
        fptr.write('\n')

    fptr.close()
