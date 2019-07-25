'''
Given a linked list, check if the the linked list has loop or not.
For example the list below contains loop:
1 -> 2 -> 3 -> 4 -> 5 -> 6
               ^         |
               |_________|
'''
from linkedlist import Node
from linkedlist import LinkedList

def hasLoop(node):
    fast, slow = node, node
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            return True
    return False

l = LinkedList()
[l.append(x) for x in range(1, 7)]
print hasLoop(l.head)
l.head.next.next.next.next.next.next = l.head.next.next.next
print hasLoop(l.head)
