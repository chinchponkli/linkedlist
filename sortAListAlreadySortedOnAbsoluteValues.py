'''
Given a linked list which is sorted based on absolute values.
Sort the list based on actual values.

Examples:

Input :  1 -> -10
output: -10 -> 1

Input : 1 -> -2 -> -3 -> 4 -> -5
output: -5 -> -3 -> -2 -> 1 -> 4

Input : -5 -> -10
Output: -10 -> -5

Input : 5 -> 10
output: 5 -> 10
'''
from linkedlist import Node
from linkedlist import LinkedList

'''
Approach
1. Segregate negative and non-negative nodes.
2. Reverse the negative part.
'''
def sort(l):
    if l.head is None or l.head.next is None:
        return
    last = l.head
    while last and last.next:
        last = last.next
    firstNonNegativeNode, current, prev = None, l.head, None
    while current and current != firstNonNegativeNode:
        if current.data < 0:
            prev, current = current, current.next
        else:
            if firstNonNegativeNode is None:
                firstNonNegativeNode = current
            if prev:
                prev.next = current.next
                last.next = current
                current.next = None
                current = prev.next
            else:
                l.head = current.next
                last.next = current
                current.next = None
                current = l.head
            last = last.next
    prev, current = None, l.head
    while current and current.data < 0:
        next = current.next
        current.next = prev
        prev, current = current, next
    if prev is not None:
        l.head.next = next
        l.head = prev

l = LinkedList()
l.append(-1)
l.append(2)
l.append(-3)
l.append(-4)
l.append(-5)
l.printList()
sort(l)
l.printList()
