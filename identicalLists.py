'''
Two Linked Lists are identical when they have same data and arrangement of data
is also same. For example Linked lists a (1->2->3) and b(1->2->3) are identical.
Write a function to check if the given two linked lists are identical.
'''
from linkedlist import LinkedList
from linkedlist import Node

def areIdentical(a, b):
    if a and b:
        return a.data == b.data and areIdentical(a.next, b.next)
    elif a or b:
        return False
    else:
        return True

l = LinkedList()
[l.append(x) for x in range(1, 8)]

print areIdentical(l.head, l.head)
