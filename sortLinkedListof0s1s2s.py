'''
Given a linked list of 0s, 1s and 2s, sort it.

Example:

    Input: 1 -> 1 -> 2 -> 0 -> 2 -> 0 -> 1 -> NULL
    Output: 0 -> 0 -> 1 -> 1 -> 1 -> 2 -> 2 -> NULL
'''
from linkedlist import LinkedList
from linkedlist import Node

def sort(node):
    a, b, c , current = 0, 0, 0, node
    while current:
        if current.data == 0:
            a += 1
        elif current.data == 1:
            b += 1
        else:
            c += 1
        current = current.next
    while node:
        if a > 0:
            node.data = 0
            a -= 1
        elif b > 0:
            node.data = 1
            b -= 1
        else:
            node.data = 2
            c -= 1
        node = node.next

l = LinkedList()
l.append(1)
l.append(1)
l.append(2)
l.append(0)
l.append(2)
l.append(0)
l.append(1)
l.printList()
sort(l.head)
l.printList()
