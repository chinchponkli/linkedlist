'''
Given a singly linked list, rotate the linked list counter-clockwise by k nodes.
Where k is a given positive integer. For example, if the given linked list is
10 -> 20 -> 30 -> 40 -> 50 -> 60 and k is 4, the list should be modified to
50 -> 60 -> 10 -> 20 -> 30 -> 40.

In case of clockwise rotation, modified list will be:
30 -> 40 -> 50 -> 60 -> 10 -> 20
'''
from linkedlist import LinkedList
from linkedlist import Node

def rotateCounterClockwise(l, k):
    k %= l.size()
    current, prev = l.head, None
    while k > 0:
        current, prev, k = current.next, current, k - 1
    if prev is None:
        return
    prev.next = None
    last = current
    while last and last.next:
        last = last.next
    last.next = l.head
    l.head = current

def rotateClockwise(l, k):
    k = (l.size() - k % l.size()) % l.size()
    current, prev = l.head, None
    while k > 0:
        current, prev, k = current.next, current, k - 1
    if prev is None:
        return
    prev.next = None
    last = current
    while last and last.next:
        last = last.next
    last.next = l.head
    l.head = current

l = LinkedList()
[l.append((i+1)*10) for i in range(6)]
l.printList()
rotateClockwise(l, 0)
l.printList()
