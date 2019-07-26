'''
Number is represented in linked list such that each digit corresponds to a node
in linked list. Increment it by 1.

For example 1999 is represented as (1-> 9-> 9 -> 9) and adding 1 to it should
change it to (2->0->0->0)
'''
from linkedlist import LinkedList
from linkedlist import Node

def increment(l):
    c = [1]
    incrementUtil(l.head, c)
    if c[0] == 1:
        l.push(1)

def incrementUtil(node, c):
    if node:
        incrementUtil(node.next, c)
        s = node.data + c[0]
        node.data = s % 10
        c[0] = s / 10

l = LinkedList()
l.append(9)
l.append(9)
l.append(9)
l.printList()
increment(l)
l.printList()
