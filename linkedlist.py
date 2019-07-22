'''
Like arrays, Linked List is a linear data structure. Unlike arrays, linked list
elements are not stored at contiguous location; the elements are linked using
pointers.
'''

'''
The first node of the linked list is called Head. Each node has some data and
points to next node. The last node points to null.
For example:
head -> 1 -> 2 -> 3 -> 4 -> 5 -> null
'''

'''
Representation:
A linked list is represented by a pointer to the first node of the linked list.
The first node is called head. If the linked list is empty, then value of head is NULL.
Each node in a list consists of at least two parts:
1) data
2) Pointer (Or Reference) to the next node
'''

'''
Below is a python implementation for linked list and its node
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        