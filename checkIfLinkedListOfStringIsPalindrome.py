'''
Given a linked list handling string data, check to see whether data is palindrome or not?
For example,

Input  : a -> bc -> d -> dcb -> a -> NULL
Output : True
String "abcddcba" is palindrome.
'''
from linkedlist import LinkedList
from linkedlist import Node

def checkPalindrome(node):
    sb = []
    while node:
        sb.append(node.data)
        node = node.next
    s = ''.join(sb)
    l = 0
    r = len(s) - 1
    while l < r:
        if s[l] == s[r]:
            l, r = l + 1, r - 1
        else:
            return False
    return True

l = LinkedList()
l.append("a")
l.append("bc")
l.append("d")
l.append("dcb")
l.append("a")

print checkPalindrome(l.head)
