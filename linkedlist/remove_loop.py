# https://practice.geeksforgeeks.org/problems/remove-loop-in-linked-list/1?page=1&sortBy=submissions

'''
# node class:

class Node:
    def __init__(self,val):
        self.next=None
        self.data=val

'''


class Solution:
    # Function to remove a loop in the linked list.
    def removeLoop(self, head):
        # code here
        # remove the loop without losing any nodes
        if head is None:
            return
        p1 = head
        p2 = head

        while True:
            if p1.next is None or p2.next is None or p2.next.next is None:
                return
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                break

        k = 0
        p3 = p1.next
        while p3 != p1:
            p3 = p3.next
            k += 1
        k += 1
        p2 = head
        for i in range(k):
            p2 = p2.next

        p3 = head

        while (p3 != p2):
            p3 = p3.next
            p2 = p2.next

        while p2.next != p3:
            p2 = p2.next
        p2.next = None
