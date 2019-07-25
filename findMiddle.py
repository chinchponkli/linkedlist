'''
Given a singly linked list, find middle of the linked list.
For example, if given linked list is 1->2->3->4->5 then output should be 3.
If there are even nodes, then there would be two middle nodes, we need to print
second middle element. For example, if given linked list is 1->2->3->4->5->6
then output should be 4.
'''
from linkedlist import Node
from linkedlist import LinkedList

def findMiddle(node):
    fast, slow = node, node
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    return slow

l = LinkedList()
[l.append(x) for x in range(1,6)]
l.printList()
middleNode = findMiddle(l.head)
print middleNode.data if middleNode else None

m = LinkedList()
[m.append(x) for x in range(1,7)]
m.printList()
middleNode = findMiddle(m.head)
print middleNode.data if middleNode else None
