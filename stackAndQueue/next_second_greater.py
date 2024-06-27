# https://leetcode.com/problems/next-greater-element-iv/
import heapq
from typing import List


class Solution:
    @staticmethod
    def secondGreaterElement(nums: List[int]) -> List[int]:
        # [1, 2, 3, 4, 9, 1, 5, 3]
        n = len(nums)
        if n < 3:
            return [-1 for _ in range(n)]

        nextNums = [[] for _ in range(n)]
        stack = [n - 1]

        for i in range(n - 2, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()
            if stack:
                nextNums[stack[-1]].append(i)
            stack.append(i)

        minheap = []
        answer = [-1 for _ in range(n)]

        for i in range(n):
            while minheap and minheap[0][0] < nums[i]:
                _, curr = heapq.heappop(minheap)
                answer[curr] = nums[i]
            for elem in nextNums[i]:
                heapq.heappush(minheap, (nums[elem], elem))

        return answer
