# https://www.geeksforgeeks.org/problems/find-the-number-of-islands/1

import sys
from collections import deque

sys.setrecursionlimit(10 ** 8)


class Solution:
    def numIslands(self, grid):
        # code here
        lands = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    lands.add((i, j))
        ans = 0
        while lands:
            ans += 1
            bfsQueue = deque()
            bfsQueue.append(next(iter(lands)))
            while bfsQueue:
                curr = bfsQueue.popleft()
                if curr not in lands:
                    continue
                lands.remove(curr)

                temp = (curr[0], curr[1] + 1)
                if temp in lands:
                    bfsQueue.append(temp)

                temp = (curr[0], curr[1] - 1)
                if temp in lands:
                    bfsQueue.append(temp)

                temp = (curr[0] + 1, curr[1] + 1)
                if temp in lands:
                    bfsQueue.append(temp)

                temp = (curr[0] + 1, curr[1])
                if temp in lands:
                    bfsQueue.append(temp)

                temp = (curr[0] + 1, curr[1] - 1)
                if temp in lands:
                    bfsQueue.append(temp)

                temp = (curr[0] - 1, curr[1] + 1)
                if temp in lands:
                    bfsQueue.append(temp)

                temp = (curr[0] - 1, curr[1])
                if temp in lands:
                    bfsQueue.append(temp)

                temp = (curr[0] - 1, curr[1] - 1)
                if temp in lands:
                    bfsQueue.append(temp)

        return ans

