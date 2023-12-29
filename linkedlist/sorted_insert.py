class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Solution:
    def sortedInsert(self, head1, key):
        # code here
        # return head of edited linked list
        if head1.data >= key:
            node = Node(key)
            node.next = head1
            return node
        temp = head1
        while temp.next:
            prev = temp
            temp = temp.next
            if temp.data >= key:
                node = Node(key)
                prev.next = node
                node.next = temp
                return head1
        temp.next = Node(key)
        return head1
