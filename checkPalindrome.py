'''
Given a singly linked list of characters, write a function that returns true
if the given list is palindrome, else false.
The list below is palindrome:
{Empty List}
1
1 -> 2 -> 2 -> 1
'''

from linkedlist import Node
from linkedlist import LinkedList

'''
Approach 1 (Using stack):
1) Traverse the given list from head to tail and push every visited node to stack.
2) Traverse the list again. For every visited node, pop a node from stack and
compare data of popped node with currently visited node.
3) If all nodes matched, then return true, else false.
Time complexity of above method is O(n), but it requires O(n) extra space.
'''

def checkPalindromeStackBased(node):
    s = []
    current = node
    while current is not None:
        s.append(current.data)
        current = current.next
    current = node
    while current is not None:
        if current.data != s.pop():
            return False
        s.append(current.data)
        current = current.next
    return True

l = LinkedList()
print checkPalindromeStackBased(l.head)
l.append(1)
print checkPalindromeStackBased(l.head)
l.append(2)
l.append(2)
l.append(1)
print checkPalindromeStackBased(l.head)
