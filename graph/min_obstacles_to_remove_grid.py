# https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/

import heapq
from typing import List
import sys


class Solution:
    @staticmethod
    def minimumObstacles(grid: List[List[int]]) -> int:

        def isValid(i, j, m, n):
            if i >= m or i < 0:
                return False
            if j >= n or j < 0:
                return False
            return True

        heap = []
        m = len(grid)
        n = len(grid[0])
        heapq.heappush(heap, (0, (0, 0)))
        arr = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        dist = [[sys.maxsize for _ in range(n)] for _ in range(m)]
        dist[0][0] = 0

        visited = set()

        while heap:
            _, curr = heapq.heappop(heap)
            if curr in visited:
                continue
            if curr == (m - 1, n - 1):
                return dist[m - 1][n - 1]
            for i in range(4):
                next_node = (curr[0] + arr[i][0], curr[1] + arr[i][1])
                if not isValid(next_node[0], next_node[1], m, n):
                    continue
                if dist[next_node[0]][next_node[1]] > dist[curr[0]][curr[1]] + grid[next_node[0]][next_node[1]]:
                    dist[next_node[0]][next_node[1]] = dist[curr[0]][curr[1]] + grid[next_node[0]][next_node[1]]
                    heapq.heappush(heap, (dist[next_node[0]][next_node[1]], next_node))

        return -1


if __name__ == "__main__":
    def test_returns_zero_for_no_obstacles():
        grid = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ]
        solution = Solution()
        assert solution.minimumObstacles(grid) == 0

    def test_calculates_minimum_obstacles_mixed_values():
        grid = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]
        result = Solution.minimumObstacles(grid)
        assert result == 2

    def test_all_cells_as_obstacles():
        grid = [[0, 1, 1], [1, 1, 1], [1, 1, 1]]
        result = Solution.minimumObstacles(grid)
        assert result == 3

    test_returns_zero_for_no_obstacles()
    test_calculates_minimum_obstacles_mixed_values()
    test_returns_zero_for_no_obstacles()


