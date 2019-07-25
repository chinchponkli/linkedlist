'''
Given a singly linked list, remove all the nodes which have a greater value on right side.

Examples:
a) The list 12 -> 15 -> 10 -> 11 -> 5 -> 6 -> 2 -> 3 -> NULL should be changed to 15 -> 11 -> 6 -> 3 -> NULL.
b) The list 10 -> 20-> 30 -> 40 -> 50 -> 60 -> NULL should be changed to 60 -> NULL.
c) The list 60 -> 50 -> 40 -> 30 -> 20 -> 10 -> NULL should not be changed.
'''
from linkedlist import LinkedList
from linkedlist import Node
from reverse import reverse

'''
1. Reverse the list.
2. Traverse the reversed list. Keep max till now. If next node is less than max,
then delete the next node, otherwise max = next node.
3. Reverse the list again to retain the original order.

Time Complexity: O(n)
'''
def deleteIfGreaterElementOnRight(l):
    maxNow = -1
    reverse(l)
    prev, current = None, l.head
    while current:
        if current.data >= maxNow:
            maxNow = current.data
            prev, current = current, current.next
        else:
            temp = current.next
            prev.next = temp
            temp = None
            current = prev.next
    reverse(l)

l = LinkedList()
l.append(12)
l.append(15)
l.append(10)
l.append(11)
l.append(5)
l.append(6)
l.append(2)
l.append(3)

l.printList()
deleteIfGreaterElementOnRight(l)
l.printList()
