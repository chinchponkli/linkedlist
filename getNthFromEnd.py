'''
Write a function that takes a linked list and an integer index and returns
the node at that index position counting from end.

Input:  1->10->30->14,  index = 2
Output: 10

For index = 5, return null. Please see that the list is zero indexed from back.
'''
from linkedlist import Node
from linkedlist import LinkedList

def getNthFromEnd(node, n):
    a, b = node, node
    while a and n > 0:
        a = a.next
        n -= 1
    if not a or n < 0:
        return None
    while a.next:
        a, b = a.next, b.next
    return b

a = LinkedList()
a.append(1)
a.append(10)
a.append(30)
a.append(14)
a.printList()
for i in range(a.size() + 1):
    nthNode = getNthFromEnd(a.head, i)
    print(nthNode.data if nthNode is not None else None)
nthNode = getNthFromEnd(a.head, -1)
print(nthNode.data if nthNode is not None else None)
