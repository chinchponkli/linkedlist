'''
Given a singly linked list of 0s and 1s find its decimal equivalent.

   Input  : 0->0->0->1->1->0->0->1->0
   Output : 50
'''
from linkedlist import Node
from linkedlist import LinkedList

def decimalEquivalent(node):
    result = 0
    while node:
        result *= 2
        result += node.data
        node = node.next
    return result

l = LinkedList()
l.append(0)
l.append(0)
l.append(0)
l.append(1)
l.append(1)
l.append(0)
l.append(0)
l.append(1)
l.append(0)
l.printList()

print decimalEquivalent(l.head)
