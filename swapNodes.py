'''
Given a linked list and two keys in it, swap nodes for two given keys.
Nodes should be swapped by changing links.
Example:
Input:  10->15->12->13->20->14,  x = 12, y = 20
Output: 10->15->20->13->12->14

You can assume that the list always contains two nodes.
'''
from linkedlist import Node
from linkedlist import LinkedList

def swapNodes(l, x, y):
    current, prev, prevX, prevY, nodeX, nodeY = l.head, None, None, None, None, None
    while current is not None:
        if current.data == x:
            prevX = prev
            nodeX = current
        if current.data == y:
            prevY = prev
            nodeY = current
        prev = current
        current = current.next

    # case: nodeX is head
    if prevX is None:
        l.head, nodeY.next, prevY.next, nodeX.next = nodeY, nodeX.next, nodeX, nodeY.next
    # case: nodeY is head    
    elif prevY is None:
        l.head, nodeX.next, prevX.next, nodeY.next = nodeX, nodeY.next, nodeY, nodeX.next
    # both are internal nodes
    else:
        prevX.next, prevY.next, nodeX.next, nodeY.next = nodeY, nodeX, nodeY.next, nodeX.next

l = LinkedList()
[l.append(i) for i in range(1, 8)]
l.printList()
swapNodes(l, 1, 7)
l.printList()
