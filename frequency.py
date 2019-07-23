'''
Given a singly linked list and a key, count number of occurrences of given key
in linked list. For example, if given linked list is 1->2->1->2->1->3->1 and
given key is 1, then output should be 4.
'''
from linkedlist import Node
from linkedlist import LinkedList

def frequency(node, key):
    count = 0
    while node is not None:
        if node.data == key:
            count += 1
        node = node.next
    return count

l = LinkedList()
l.append(1)
l.append(2)
l.append(1)
l.append(2)
l.append(1)
l.append(3)
l.append(1)

l.printList()

print "Count of 1: " + str(frequency(l.head, 1))
print "Count of 2: " + str(frequency(l.head, 2))
print "Count of 3: " + str(frequency(l.head, 3))
print "Count of 4: " + str(frequency(l.head, 4))
