'''
Write a removeDuplicates() function which takes a list and deletes any duplicate
nodes from the list. The list is not sorted.
For example if the linked list is 12->11->12->21->41->43->21 then
removeDuplicates() should convert the list to 12->11->21->41->43.
'''
from linkedlist import Node
from linkedlist import LinkedList

def removeDuplicates(node):
    prev = None
    s = set()
    while node:
        if node.data in s:
            prev.next = node.next
        else:
            s.add(node.data)
            prev = node
        node = node.next

l = LinkedList()
[l.append(12) for i in range(2)]
l.insertAfter(l.head, 11)
l.append(21)
l.append(41)
l.append(43)
l.append(21)

l.printList()
removeDuplicates(l.head)
l.printList()
