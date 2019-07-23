'''
Write a function that searches a given key 'x' in a given singly linked list.
The function should return true if x is present in linked list and false otherwise.
For example, if the key to be searched is 15 and linked list is
14->21->11->30->10, then function should return false.
If key to be searched is 14, then the function should return true.
'''
from linkedlist import Node
from linkedlist import LinkedList

def search(node, key):
    while node:
        if node.data == key:
            return True
        node = node.next
    return False

l = LinkedList()
l.append(14)
l.append(21)
l.append(11)
l.append(30)
l.append(10)

l.printList()
print ("Is 14 in the list? : " + str(search(l.head, 14)))
print ("Is 15 in the list? : " + str(search(l.head, 15)))
