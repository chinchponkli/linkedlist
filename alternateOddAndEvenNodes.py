'''
Given a singly linked list, rearrange the list so that even and odd nodes are
alternate in the list.
There are two possible forms of this rearrangement. If the first data is odd,
then the second node must be even. The third node must be odd and so on.
Notice that another arrangement is possible where the first node is even, s
econd odd, third even and so on.
Please note that the number of odd and even nodes are equal.
Examples:
Input : 11 -> 20 -> 40 -> 55 -> 77 -> 80 -> NULL
Output : 11 -> 20 -> 55 -> 40 -> 77 -> 80 -> NULL
20, 40, 80 occur in even positions and 11, 55, 77
occur in odd positions.
Input : 10 -> 1 -> 2 -> 3 -> 5 -> 6 -> 7 -> 8 -> NULL
Output : 1 -> 10 -> 3 -> 2 -> 5 -> 6 -> 7 -> 8 -> NULL
1, 3, 5, 7 occur in odd positons and 10, 2, 6, 8 occur
at even positions in the list
'''
from linkedlist import Node
from linkedlist import LinkedList

'''
Approach:
1. Segregate list into even and odd.
2. Merge two lists in place.
'''
def alternateOddAndEvenNodes(l):
    last = l.head
    while last and last.next:
        last = last.next
    current, prev, firstOddNode = l.head, None, None
    while current and current != firstOddNode:
        if current.data % 2 == 0:
            prev, current = current, current.next
        else:
            if not firstOddNode:
                firstOddNode = current
            if prev:
                prev.next = current.next
                last.next = current
                current.next = None
                current = prev.next
            else:
                l.head = current.next
                last.next = current
                current.next = None
                current = l.head
            last = last.next
    if not prev:
        return
    prev.next = None
    current, oddNode = l.head, firstOddNode
    while oddNode:
        current.next, oddNode.next, current, oddNode = oddNode, current.next, current.next, oddNode.next

l = LinkedList()
l.append(11)
l.append(20)
l.append(40)
l.append(55)
l.append(77)
l.append(80)

l.printList()
alternateOddAndEvenNodes(l)
l.printList()
