'''
1. Merge two sorted linked lists such that merged list is in sorted order.
Given two linked lists sorted in increasing order. Merge them such a way that
the result list is in sorted order.
Examples:
Input:  a: 5->10->15->40
        b: 2->3->20
Output: res: 2->3->5->10->15>20->40
2. Merge two sorted linked lists such that merged list is in reverse order.
Given two linked lists sorted in increasing order. Merge them such a way that
the result list is in decreasing order.
Examples:
Input:  a: 5->10->15->40
        b: 2->3->20
Output: res: 40->20->15->10->5->3->2
'''
from linkedlist import LinkedList
from linkedlist import Node

def mergeSorted(a, b):
    l = LinkedList()
    while a and b:
        if a.data == b.data:
            l.append(a.data)
            a, b = a.next, b.next
        elif a.data < b.data:
            l.append(a.data)
            a = a.next
        else:
            l.append(b.data)
            b = b.next
    while a:
        l.append(a.data)
        a = a.next
    while b:
        l.append(b.data)
        b = b.next
    return l

def mergeSortedReverse(a, b):
    l = LinkedList()
    while a and b:
        if a.data == b.data:
            l.push(a.data)
            a, b = a.next, b.next
        elif a.data < b.data:
            l.push(a.data)
            a = a.next
        else:
            l.push(b.data)
            b = b.next
    while a:
        l.push(a.data)
        a = a.next
    while b:
        l.push(b.data)
        b = b.next
    return l

l1 = LinkedList()
l1.append(5)
l1.append(10)
l1.append(15)
l1.append(40)
l1.printList()

l2 = LinkedList()
l2.append(2)
l2.append(3)
l2.append(20)
l2.printList()

mergedList = mergeSorted(l1.head, l2.head)
reverseMergedList = mergeSortedReverse(l1.head, l2.head)
mergedList.printList()
reverseMergedList.printList()
