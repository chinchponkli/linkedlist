'''
Intersection of two Sorted Linked Lists
Given two lists sorted in increasing order, create and return a new list
representing the intersection of the two lists. The new list should be made with
its own memory - the original lists should not be changed.
For example, let the first linked list be 1->2->3->4->6 and second linked list
be 2->4->6->8, then your function should create and return a third list as
2->4->6.
'''
from linkedlist import Node
from linkedlist import LinkedList

def intersection(a, b):
    l = LinkedList()
    while a is not None and b is not None:
        if a.data == b.data:
            l.append(a.data)
            a, b = a.next, b.next
        elif a.data < b.data:
            a = a.next
        else:
            b = b.next
    return l

l1 = LinkedList()
[l1.append(i) for i in range(1, 7)]
l2 = LinkedList()
[l2.append(2 * i) for i in range(1, 5)]
l1.printList()
l2.printList()
intersection(l1.head, l2.head).printList()
