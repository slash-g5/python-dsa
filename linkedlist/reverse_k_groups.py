# https://leetcode.com/problems/reverse-nodes-in-k-group/
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node


class Solution:
    @staticmethod
    def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 1:
            return head
        start = head
        p_end = None
        first = True

        while 1:
            if start:
                print(f'{start.val=}')
            if not p_end:
                print('p_end=None')
            else:
                print(f'{p_end.val=}')
            if start is None:
                break
            # if p_end:
            #     p_end.next = start
            check = start
            for i in range(k - 1):
                check = check.next
                if check is None:
                    if p_end:
                        p_end.next = start
                    return head

            curr = start
            prev = None
            for i in range(k):
                if curr is None:
                    start = None
                    break
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            if first:
                head = prev
                first = False
            if p_end:
                p_end.next = prev
            p_end = start
            if start:
                start = curr

        return head
