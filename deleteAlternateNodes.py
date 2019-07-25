'''
Given a Singly Linked List, starting from the second node delete all alternate
nodes of it. For example, if the given linked list is 1->2->3->4->5 then your
function should convert it to 1->3->5, and if the given linked list is
1->2->3->4 then convert it to 1->3.
'''
from linkedlist import LinkedList
from linkedlist import Node

def deleteAlternateNodes(node):
    while node is not None and node.next is not None:
        temp = node.next
        node.next = temp.next
        temp = None
        node = node.next

l = LinkedList()
[l.append(x) for x in range(1, 7)]
l.printList()
deleteAlternateNodes(l.head)
l.printList()
