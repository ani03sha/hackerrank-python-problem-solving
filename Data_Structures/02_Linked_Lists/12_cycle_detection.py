# A linked list is said to contain a cycle if any node is visited more than once while traversing the list.
#
# Complete the function provided for you in your editor. It has one parameter: a pointer to a Node object named head
# that points to the head of a linked list. Your function must return a boolean denoting whether or not there is a
# cycle in the list. If there is a cycle, return true; otherwise, return false.
#
# Note: If the list is empty, head will be null.


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


def has_cycle(head):
    if not head:
        return False

    slow = head
    fast = head

    # If slow and fast pointers meet somewhere then there is loop
    while slow and fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True

    return False


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    tests = int(input())

    for tests_itr in range(tests):
        index = int(input())

        llist_count = int(input())

        llist = SinglyLinkedList()

        for _ in range(llist_count):
            llist_item = int(input())
            llist.insert_node(llist_item)

        extra = SinglyLinkedListNode(-1);
        temp = llist.head;

        for i in range(llist_count):
            if i == index:
                extra = temp

            if i != llist_count - 1:
                temp = temp.next

        temp.next = extra

        result = has_cycle(llist.head)

        fptr.write(str(int(result)) + '\n')

    fptr.close()
