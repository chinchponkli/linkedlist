'''
Given a linked list, write a function to reverse every alternate k nodes in an
efficient way.
Example:
Inputs:   1->2->3->4->5->6->7->8->9->NULL and k = 3
Output:   3->2->1->4->5->6->9->8->7->NULL.
'''
from linkedlist import LinkedList
from linkedlist import Node

def reverseAlternateKNodes(node, k, reverse):
    prev, current, count, next = None, node, 0, None
    while current and count < k:
        if reverse:
            next = current.next
            current.next = prev
            prev, current = current, next
            count += 1
        else:
            prev, current, next = current, current.next, current.next
            count += 1
    if reverse:
        if next:
            node.next = reverseAlternateKNodes(next, k, not reverse)
    else:
        if prev:
            prev.next = reverseAlternateKNodes(next, k, not reverse)
    return prev if reverse else node

l = LinkedList()
[l.append(x) for x in range(1, 10)]
l.printList()
l.head = reverseAlternateKNodes(l.head, 3, True)
l.printList()
