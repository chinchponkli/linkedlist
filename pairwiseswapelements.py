'''
Given a singly linked list, write a function to swap elements pairwise.
For example, if the linked list is 1->2->3->4->5 then the function should
change it to 2->1->4->3->5, and if the linked list is 1->2->3->4->5->6 then the
function should change it to 2->1->4->3->6->5.
'''
from linkedlist import Node
from linkedlist import LinkedList

def pairwiseSwap(node):
    while node and node.next:
        node.data, node.next.data = node.next.data, node.data
        node = node.next.next

l = LinkedList()
[l.append(x) for x in range(1, 6)]
l.printList()
pairwiseSwap(l.head)
l.printList()
