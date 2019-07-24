'''
Write a function which takes a list sorted in non-decreasing order and deletes
any duplicate nodes from the list. The list should only be traversed once.
For example if the linked list is 11->11->11->21->43->43->60 then
removeDuplicates() should convert the list to 11->21->43->60.
'''
from linkedlist import Node
from linkedlist import LinkedList

def removeDuplicates(node):
    while node and node.next:
        if node.data == node.next.data:
            temp = node.next
            node.next = temp.next
            temp = None
        else:
            node = node.next

l = LinkedList()
[l.append(11) for i in range(3)]
l.append(21)
[l.append(43) for i in range(2)]
l.append(60)

l.printList()
removeDuplicates(l.head)
l.printList()
