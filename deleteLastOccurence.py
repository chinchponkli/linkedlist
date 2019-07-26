'''
Input:   1->2->3->5->2->10, key = 2
Output:  1->2->3->5->10
'''
from linkedlist import LinkedList
from linkedlist import Node

def deleteLast(l, key):
    current, lastNode, prev, lastNodePrev = l.head, None, None, None
    while current:
        if current.data == key:
            lastNodePrev = prev
            lastNode = current
        prev, current = current, current.next
    if lastNode is None:
        return
    if lastNodePrev is None:
        l.head = l.head.next
        lastNode = None
    else:
        lastNodePrev.next = lastNode.next
        lastNode = None

l = LinkedList()
l.append(1)
l.append(2)
l.append(3)
l.append(5)
l.append(2)
l.append(10)
l.printList()
deleteLast(l, 10)
l.printList()
