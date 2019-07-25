'''
Given two numbers represented by two lists, write a function that returns the
sum list. The sum list is list representation of the addition of two input numbers.

Example:

Input: List1: 5 -> 6 -> 3  // represents number 365
       List2: 8 -> 4 -> 2 //  represents number 248
Output: Resultant list: 3 -> 1 -> 6  // represents number 613


Input: List1: 7 -> 5 -> 9 -> 4 -> 6  // represents number 64957
       List2: 8 -> 4 //  represents number 48
Output: Resultant list: 5 -> 0 -> 0 -> 5 -> 6  // represents number 65005
'''
from linkedlist import LinkedList
from linkedlist import Node

def add(a, b):
    sumList = LinkedList()
    carry = 0
    while a or b:
        x = a.data if a else 0
        y = b.data if b else 0
        cSum = carrySum(x, y, carry)
        carry, sum = cSum[0], cSum[1]
        sumList.append(sum)
        if a:
            a = a.next
        if b:
            b = b.next
    if carry == 1:
        sumList.append(1)
    return sumList

def carrySum(x, y, carry):
    sum = (x + y + carry)
    return (sum / 10, sum % 10)

a = LinkedList()
a.append(7)
a.append(5)
a.append(9)
a.append(4)
a.append(6)


b = LinkedList()


add(a.head, b.head).printList()
