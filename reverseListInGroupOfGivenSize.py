'''
Given a linked list, write a function to reverse every k nodes.
Example:
Inputs:  1->2->3->4->5->6->7->8->NULL and k = 3
Output:  3->2->1->6->5->4->8->7->NULL.
Inputs:   1->2->3->4->5->6->7->8->NULL and k = 5
Output:  5->4->3->2->1->8->7->6->NULL.
'''

from linkedlist import Node
from linkedlist import LinkedList

def reverse(node, k):
    prev, current, count = None, node, 0
    while current and count < k:
        next = current.next
        current.next = prev
        prev, current = current, next
        count += 1
    '''
    Now either next is null in that case we just return prev to be made as head
    Else it points to (k+1)th node. Intital node's next will point to the reverse
    of the next segment of the list. Simple.
    '''
    if next:
        node.next = reverse(next, k)
    return prev

l = LinkedList()
[l.append(x) for x in range(1, 9)]
l.printList()
l.head = reverse(l.head, 3)
l.printList()
