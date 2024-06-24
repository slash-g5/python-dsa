# https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/

import heapq
from typing import List


class Solution:
    @staticmethod
    def minimumTime(grid: List[List[int]]) -> int:
        def isValid(index, m, n):
            return 0 <= index[0] < m and 0 <= index[1] < n

        if grid[0][0] > 0:
            return -1

        m = len(grid)
        n = len(grid[0])

        if m == 1 and n == 1:
            return 0

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        consider_0 = grid[0][1] <= 1 or grid[1][0] <= 1

        visited = set()

        my_heap = []
        heapq.heappush(my_heap, (0, (0, 0)))

        while my_heap:
            c_time, c_index = heapq.heappop(my_heap)
            if c_index in visited:
                continue
            visited.add(c_index)
            if c_index == (m - 1, n - 1):
                return c_time
            for i in range(4):
                n_index = (c_index[0] + directions[i][0], c_index[1] + directions[i][1])
                if n_index in visited:
                    continue
                if isValid(n_index, m, n) and grid[n_index[0]][n_index[1]] <= c_time + 1:
                    heapq.heappush(my_heap, (c_time + 1, n_index))
                elif isValid(n_index, m, n) and (consider_0 or c_index != (0, 0)):
                    heapq.heappush(my_heap, (
                        grid[n_index[0]][n_index[1]] + (grid[n_index[0]][n_index[1]] - c_time - 1) % 2, n_index))

        return -1
