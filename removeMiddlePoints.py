'''
Given a linked list of line segments, remove middle points

Given a linked list of co-ordinates where adjacent points either form a vertical
line or a horizontal line. Delete points from the linked list which are in the
middle of a horizontal or vertical line.

Examples:

Input:  (0,10)->(1,10)->(5,10)->(7,10)
                                  |
                                (7,5)->(20,5)->(40,5)
Output: Linked List should be changed to following
        (0,10)->(7,10)
                  |
                (7,5)->(40,5)
The given linked list represents a horizontal line from (0,10)
to (7, 10) followed by a vertical line from (7, 10) to (7, 5),
followed by a horizontal line from (7, 5) to (40, 5).

Input:     (2,3)->(4,3)->(6,3)->(10,3)->(12,3)
Output: Linked List should be changed to following
    (2,3)->(12,3)
There is only one vertical line, so all middle points are removed.
'''
from linkedlist import LinkedList
from linkedlist import Node

def removeMiddlePoints(node):
    while node and node.next and node.next.next:
        if (node.data[0] == node.next.data[0] and node.data[0] == node.next.next.data[0]):
            node.next = node.next.next
        elif (node.data[1] == node.next.data[1] and node.data[1] == node.next.next.data[1]):
            node.next = node.next.next
        else:
            node = node.next

l = LinkedList()
l.append((0, 10))
l.append((1, 10))
l.append((5, 10))
l.append((7, 10))
l.append((7, 5))
l.append((20, 5))
l.append((40, 5))
l.printList()
removeMiddlePoints(l.head)
l.printList()
