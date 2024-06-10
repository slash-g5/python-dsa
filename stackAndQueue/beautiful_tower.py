# https://leetcode.com/problems/beautiful-towers-i/
import sys
from typing import List
class Solution:
    def maximumSumOfHeights(self, heights: List[int]) -> int:

        def sumTillArray(arr):
            sumArr = []
            for a in arr:
                if not sumArr:
                    sumArr.append(a)
                    continue
                sumArr.append(sumArr[-1] + a)
            return sumArr

        def bricksBetween(arr, start, end, peak):
            if start > end:
                return 0
            if start <= 0:
                return arr[end] - peak*(end+1)
            return (arr[end] - arr[start-1]) - peak*(end - start +1)


        sumTill = sumTillArray(heights)

        n = len(heights)

        afterBrick = [0 for _ in range(n)]
        beforeBrick = [0 for _ in range(n)]

        stack = []

        for i in range(n):
            while stack and stack[-1][0] >= heights[i]:
                stack.pop()
            curr = 0
            if stack:
                curr += beforeBrick[stack[-1][1]]
                curr += bricksBetween(sumTill, stack[-1][1]+1, i-1, heights[i])
            else:
                curr += bricksBetween(sumTill, 0, i-1, heights[i])
            beforeBrick[i] = curr
            stack.append((heights[i], i))

        stack = []

        for i in range(n-1, -1, -1):
            while stack and stack[-1][0] >= heights[i]:
                stack.pop()
            curr = 0
            if stack:
                curr += afterBrick[stack[-1][1]]
                curr += bricksBetween(sumTill, i+1, stack[-1][1]-1, heights[i])
            else:
                curr += bricksBetween(sumTill, i+1, n-1, heights[i])
            afterBrick[i] = curr
            stack.append((heights[i], i))

        final_ans = sys.maxsize

        for i in range(n):
            final_ans = min(final_ans, (afterBrick[i]+beforeBrick[i]))

        return sumTill[-1] - final_ans