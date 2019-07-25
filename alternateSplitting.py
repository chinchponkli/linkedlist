'''
Write a function alternatingSplit() that takes one list and divides up its nodes
to make two smaller lists 'a' and 'b'. The sublists should be made from
alternating elements in the original list. So if the original list is
0->1->0->1->0->1 then one sublist should be 0->0->0
and the other should be 1->1->1.
'''
from linkedlist import Node
from linkedlist import LinkedList

def alternateSplit(l):
    l1 = LinkedList()
    lastL1 = None
    current = l.head
    while current is not None and current.next is not None:
        next = current.next
        current.next = next.next
        if l1.head is None:
            l1.head = next
        else:
            last.next = next
        next.next = None
        last = next
        current = current.next
    return (l, l1)

l = LinkedList()
l.append(0)
l.append(1)
l.append(0)
l.append(1)
l.append(0)

l.printList()
lp = alternateSplit(l)
lp[0].printList()
lp[1].printList()
