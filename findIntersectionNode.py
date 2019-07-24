'''
There are two singly linked lists in a system. By some programming error,
the end node of one of the linked list got linked to the second list,
forming an inverted Y shaped list. Write a program to get the point where two
linked list merge.
            3
             \
              6
               \
                9   10
                 \  /
                  15
                   |
                   30
In the above diagram the two linked lists intersect at node 15.
'''
from linkedlist import Node
from linkedlist import LinkedList

'''
Approach 1
1. Find length of two linked lists. Let they by l1 and l2. Let l2 >= l1.
2. Traverse (l2 - l1) nodes in larger list.
3. Now traverse both the lists and compare nodes. If they are equal that is the
intersection point.
Time Complexity: O(l1 + l2)
Space Complexity: O(1)
'''
def findIntersectionNode(a, b):
    l1 = a.size()
    l2 = b.size()
    diff = abs(l2 - l1)
    longerList = a if (l1 > l2) else b
    shorterList = b if (l1 > l2) else b
    nodeA, nodeB = longerList.head, shorterList.head
    while diff > 0:
        nodeA = nodeA.next
        diff -= 1
    while nodeA is not None:
        if nodeA == nodeB:
            return nodeA
        nodeA = nodeA.next
        nodeB = nodeB.next
    return None

l1 = LinkedList()
l1.append(3)
l1.append(6)
l1.append(9)
l1.append(15)
l1.append(30)

l2 = LinkedList()
l2.append(10)
l2.head.next = l1.head.next.next.next

intersectionNode = findIntersectionNode(l1, l2)
print intersectionNode.data if intersectionNode is not None else None
