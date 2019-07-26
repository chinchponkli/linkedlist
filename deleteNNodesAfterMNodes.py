'''
Given a linked list and two positiveintegers M and N. Traverse the linked list
such that you retain M nodes then delete next N nodes, continue the same till end of the
linked list.

Difficulty Level: Rookie

Examples:

Input:
M = 2, N = 2
Linked List: 1->2->3->4->5->6->7->8
Output:
Linked List: 1->2->5->6

Input:
M = 3, N = 2
Linked List: 1->2->3->4->5->6->7->8->9->10
Output:
Linked List: 1->2->3->6->7->8

Input:
M = 1, N = 1
Linked List: 1->2->3->4->5->6->7->8->9->10
Output:
Linked List: 1->3->5->7->9
'''
from linkedlist import LinkedList
from linkedlist import Node

def deleteNAfterM(l, N, M):
    prev, current = None, l.head
    while current:
        n, m = N, M
        while current and m > 0:
            prev, current = current, current.next
            m -= 1
        while current and n > 0:
            prev.next, current = current.next, current.next
            n -= 1

l = LinkedList()
[l.append(i+1) for i in range(8)]
l.printList()
deleteNAfterM(l, 2, 2)
l.printList()
l.delete()
l.printList()
[l.append(i+1) for i in range(10)]
l.printList()
deleteNAfterM(l, 2, 3)
l.printList()
l.delete()
l.printList()
[l.append(i+1) for i in range(10)]
l.printList()
deleteNAfterM(l, 1, 1)
l.printList()
