'''
Given a linked list, check if the the linked list contains loop or not.
For example the list below contains loop:
1 -> 2 -> 3 -> 4 -> 5 -> 6
               ^          |
               |__________|
If the linked list contains loop return its length (3 in above case),
else return 0.
'''
from linkedlist import Node
from linkedlist import LinkedList

def loopLength(node):
    fast, slow = node, node
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break
    if fast is None or fast.next is None:
        return 0
    count = 1
    a = slow.next
    while a != slow:
        count += 1
        a = a.next
    return count

l = LinkedList()
[l.append(x) for x in range(1, 7)]
print loopLength(l.head)
l.head.next.next.next.next.next.next = l.head.next.next.next
print loopLength(l.head)
