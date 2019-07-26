'''
Given a singly linked list, write a function to swap elements pairwise.
For example, if the linked list is 1->2->3->4->5 then the function should
change it to 2->1->4->3->5, and if the linked list is 1->2->3->4->5->6 then the
function should change it to 2->1->4->3->6->5.
'''
from linkedlist import LinkedList
from linkedlist import Node

def pairwiseSwap(l):
    fast, prev = l.head, None
    while fast and fast.next:
        if fast == l.head:
            next = fast.next.next
            l.head = fast.next
            fast.next.next = fast
            fast.next = next
            prev, fast = fast, fast.next
        else:
            next = fast.next.next
            prev.next = fast.next
            fast.next.next = fast
            fast.next = next
            prev, fast = fast, fast.next



l = LinkedList()
[l.append(i+1) for i in range(7)]
l.printList()
pairwiseSwap(l)
l.printList()
