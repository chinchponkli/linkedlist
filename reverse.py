'''
Given pointer to the head node of a linked list, the task is to reverse the
linked list. We need to reverse the list by changing links between nodes.
Input : Head of following linked list
       1->2->3->4->NULL
Output : Linked list should be changed to,
       4->3->2->1->NULL
'''
from linkedlist import LinkedList
from linkedlist import Node

def reverse(l):
    prev, current = None, l.head
    while current is not None:
        current.next, prev, current = prev, current, current.next
    l.head = prev

l = LinkedList()
[l.append(x) for x in range(1, 5)]
l.printList()
reverse(l)
l.printList()
