'''
Point arbit pointer to greatest value right side node in a linked list

Given singly linked list with every node having an additional "rando,"
pointer that currently points to NULL. We need to make the "random" pointer
to greatest value node in a linked list on its right side.
'''
from linkedlist import LinkedList
from linkedlist import Node
from reverse import reverse

def fillRandomPointer(l):
    if l.head is None or l.head.next is None:
        return
    maxNode = None
    reverse(l)
    current = l.head
    while current and current.data:
        if maxNode and maxNode.data > current.data:
            current.random = maxNode
        else:
            maxNode = current
        current = current.next
    reverse(l)

l = LinkedList()
l.append(1)
l.append(2)
l.append(3)
l.append(4)
l.printList()
fillRandomPointer(l)
l.printList()
node = l.head
while node:
    print str(node.data) + ".random ->",
    print node.random.data if node.random else None
    node = node.next
