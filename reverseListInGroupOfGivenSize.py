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
    while current is not None and count < k:
        next = current.next
        current.next = prev
        prev, current = current, next
        count += 1
    '''
    Now either next is null in that case we just return prev to be made as head
    Else it points to (k+1)th node. Intital node's next will point to the reverse
    of the next segment of the list. Simple.
    '''
    if next is not None:
        node.next = reverse(next, k)
    return

'''
Firstly, push the k elements of the linked list in the stack.
Now pop elements one by one and keep track of the previously popped node.
Point the next pointer of prev node to top element of stack.
Repeat this process, until NULL is reached.

This algorithm uses O(k) extra space.
'''
def reverseStackBased(l, k):
    s = []
    prev, current = None, l.head
    while current is not None:
        count = 0
        while current is not None and count < k:
            s.append(current)
            current = current.next
            count += 1
        while len(s) > 0:
            if prev is not None:
                prev.next = s[len(s) - 1]
                prev = prev.next
                s.pop()
            else:
                prev = s[len(s) - 1]
                l.head = prev
                s.pop()
    prev.next = None

l = LinkedList()
[l.append(x) for x in range(1, 10)]
l.printList()
reverseStackBased(l, 3)
l.printList()
