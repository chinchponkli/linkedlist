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

'''
Approach 1 (Finding middle of list and reversing and checking and reversing again):
1) If list is empty or has only one node return True.
2) If number of nodes are even, reverse the list from midNode else reverse
the list from midNode.next.
3) Traverse the two segments and compare.
4) Reverse the second segment again.
Time complexity of above method is O(n), but it requires O(n) extra space.
'''
def checkPalindrome(node):
    if node is None or node.next is None:
        return True
    fast, middle, preMiddle = node, node, None
    l = 0
    while fast is not None and fast.next is not None:
        l += 2
        fast, preMiddle, middle = fast.next.next, middle, middle.next
    if fast is not None:
        l += 1
    r = reverse(middle)
    revNode = r
    while node and revNode:
        if node.data != revNode.data:
            preMiddle.next = reverse(r)
            return False
        node, revNode = node.next, revNode.next
    preMiddle.next = reverse(r)
    return True

def reverse(node):
    prev = None
    while node:
        node.next, prev, node = prev, node, node.next
    return prev

l = LinkedList()
print checkPalindrome(l.head)
l.append(1)
print checkPalindrome(l.head)
l.append(2)
l.append(3)
print checkPalindrome(l.head)
l.append(2)
l.append(1)
print checkPalindrome(l.head)
