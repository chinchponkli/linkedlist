'''
Given two linked lists, represented as linked lists (every character is a node
in linked list). Write a function compare() that works similar to strcmp()
, i.e., it returns 0 if both strings are same, 1 if first linked list is
lexicographically greater, and -1 if second string is lexicographically greater

Input: list1 = g->e->e->k->s->a
       list2 = g->e->e->k->s->b
Output: -1

Input: list1 = g->e->e->k->s->a
       list2 = g->e->e->k->s
Output: 1

Input: list1 = g->e->e->k->s
       list2 = g->e->e->k->s
Output: 0
'''
from linkedlist import LinkedList
from linkedlist import Node

def strcmp(a, b):
    while a and b:
        if ord(a.data.lower()) == ord(b.data.lower()):
            a, b = a.next, b.next
        elif ord(a.data.lower()) > ord(b.data.lower()):
            return 1
        else:
            return -1
    if a:
        return 1
    if b:
        return -1
    return 0

l1 = LinkedList()
l1.append('g')
l1.append('e')
l1.append('e')
l1.append('k')
l1.append('s')

l2 = LinkedList()
l2.append('g')
l2.append('e')
l2.append('e')
l2.append('k')
l2.append('s')

l1.printList()
l2.printList()

print strcmp(l1.head, l2.head)
