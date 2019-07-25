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
from reverse import reverse

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

'''
Approach 2:
1) Let X be the length of the first linked list until intersection point.
   Let Y be the length of the second linked list until the intersection point.
   Let Z be the length of the linked list from the intersection point to End of
   the linked list including the intersection node.
   We Have
           X + Z = C1;
           Y + Z = C2;
2) Reverse first linked list.
3) Traverse Second linked list. Let C3 be the length of second list - 1.
     Now we have
        X + Y = C3
     We have 3 linear equations. By solving them, we get
       X = (C1 + C3 - C2)/2
       Y = (C2 + C3 - C1)/2
       Z = (C1 + C2 - C3)/2
      WE GOT THE INTERSECTION POINT.
4)  Reverse first linked list.
'''
def intersectionPoint(l1, l2):
    c1 = l1.size()
    c2 = l2.size()
    reverse(l1)
    c3 = l2.size() - 1
    reverse(l1)
    p = (c1 + c3 - c2) / 2
    node = l1.head
    while p > 0:
        node = node.next
        p -= 1
    return node

l1 = LinkedList()
l1.append(3)
l1.append(6)
l1.append(9)
l1.append(15)
l1.append(30)

l2 = LinkedList()
l2.append(10)
l2.head.next = l1.head.next.next.next

intersectionNode = intersectionPoint(l1, l2)
print intersectionNode.data if intersectionNode is not None else None
