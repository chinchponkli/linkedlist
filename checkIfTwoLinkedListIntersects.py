'''
Given two singly linkedlists. Check if they intersect or not.
Let the two lists be:
1 -> 2 -> 3 -> 4 -> 5 -> 6
        /
      0
'''
from linkedlist import LinkedList
from linkedlist import Node

'''
Approach.
Simply find last nodes of both and check if they are equal
'''
def checkIntersection(a, b):
    while a and a.next:
        a = a.next
    while b and b.next:
        b = b.next
    return a == b

l1 = LinkedList()
[l1.append(x+1) for x in range(6)]
l2 = LinkedList()
l2.append(0)
l2.head.next = l1.head.next.next

print checkIntersection(l1.head, l2.head)
