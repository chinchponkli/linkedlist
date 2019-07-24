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

    # Inserts new node at the head of the list
    def push(self, data):
        newNode = Node(data)
        newNode.next = self.head
        self.head = newNode

    # Inserts new node at the end of the list
    def append(self, data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
        else:
            last = self.head
            while last.next is not None:
                last = last.next
            last.next = newNode

    # Inserts a new node after prevNode
    def insertAfter(self, prevNode, data):
        if prevNode is None:
            return
        newNode = Node(data)
        newNode.next = prevNode.next
        prevNode.next = newNode

    # Does not work if the linked list has loop
    def printList(self):
        print "head ->",
        current = self.head
        while current is not None:
            print str(current.data) + " ->",
            current = current.next
        print "null"

    # Deletes the first node where key == node.data
    def deleteKey(self, key):
        if self.head is None:
            return
        if self.head.data == key:
            temp = self.head
            self.head = temp.next
            temp = None
        else:
            prev = self.head
            temp = prev.next
            while temp is not None:
                if key == temp.data:
                    break
                prev = temp
                temp = temp.next
            if temp is not None:
                prev.next = temp.next
                temp = None

    # Deletes the node at position in zero-indexed list
    def deleteAt(self, position):
        if position < 0 or self.head is None:
            return
        if position == 0:
            temp = self.head
            self.head = temp.next
            temp = None
        else:
            prev = self.head
            temp = prev.next
            count = 1
            while temp is not None:
                if count == position:
                    break
                prev = temp
                temp = temp.next
                count += 1
            if temp is not None:
                prev.next = temp.next
                temp = None

    # delete all nodes in the list
    def delete(self):
        while self.head is not None:
            self.deleteAt(0)

    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def printReverse(self):
        print "null",
        self.printReverseUtil(self.head)
        print "<- head"

    def printReverseUtil(self, node):
        if node is not None:
            self.printReverseUtil(node.next)
            print "<-",
            print node.data,
