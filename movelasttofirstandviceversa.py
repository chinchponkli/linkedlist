'''
Write a function that moves the last element to the front in a given Singly
Linked List. For example, if the given Linked List is 1->2->3->4->5, then the
function should change the list to 5->1->2->3->4.

Also write a function that moves the front element to the last.
'''
from linkedlist import Node
from linkedlist import LinkedList

def moveLastToFront(l):
    secondLast, last = None, l.head
    while last is not None and last.next is not None:
        secondLast = last
        last = last.next
    if secondLast is not None:
        secondLast.next = None
        last.next = l.head
        l.head = last

def moveFrontToLast(l):
    last = l.head
    while last is not None and last.next is not None:
        last = last.next
    if last is not None:
        last.next = l.head
        l.head = l.head.next
        last.next.next = None

l = LinkedList()
[l.append(i) for i in range(1, 6)]
l.printList()
moveLastToFront(l)
l.printList()
moveFrontToLast(l)
l.printList()
