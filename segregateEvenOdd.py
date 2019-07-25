'''
Given a Linked List of integers, write a function to modify the linked list such
that all even numbers appear before all the odd numbers in the modified linked
list. Also, keep the order of even and odd numbers same.
Examples:
Input: 17->15->8->12->10->5->4->1->7->6->NULL
Output: 8->12->10->4->6->17->15->5->1->7->NULL
Input: 8->12->10->5->4->1->6->NULL
Output: 8->12->10->4->6->5->1->NULL
// If all numbers are even then do not change the list
Input: 8->12->10->NULL
Output: 8->12->10->NULL
// If all numbers are odd then do not change the list
Input: 1->3->5->7->NULL
Output: 1->3->5->7->NULL
'''
from linkedlist import LinkedList
from linkedlist import Node

'''
Approach
1. Find last node.
2. Initialize firstddNode and prev as None. This will store firstOdd node
in the list.
3. Initialize current as head.
4. Traverse the list till the list is empty or you reencounter firstOddNode again.
5. If current node is even, update prev node to current and current to current's next.
6. If current node is odd:
    i. If firstOddNode is none save it.
    ii. Move the current node to end of the list.
    iii. Update last to this one.
'''
def segregateEvenOdd(l):
    last = l.head
    while last and last.next:
        last = last.next
    firstOddNode, prev, current = None, None, l.head
    while current and current != firstOddNode:
        if current.data % 2 == 0:
            prev = current
            current = current.next
        else:
            if not firstOddNode:
                firstOddNode = current
            if not prev:
                l.head = current.next
                last.next = current
                current.next = None
                current = l.head
            else:
                prev.next = current.next
                last.next = current
                current.next = None
                current = prev.next
            last = last.next

l = LinkedList()
l.append(17)
l.append(15)
l.append(8)
l.append(12)
l.append(10)
l.append(5)
l.append(4)
l.append(1)
l.append(7)
l.append(6)

l.printList()
segregateEvenOdd(l)
l.printList()
