# https://www.geeksforgeeks.org/problems/minimum-cost-path3833/1
import heapq


class Solution:

    # Function to return the minimum cost to react at bottom
    # right cell from top left cell.
    @staticmethod
    def minimumCostPath(grid):

        def indexValid(grid, x, y, visited):
            if (x, y) in visited:
                return False
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]):
                return False
            return True

        if len(grid) == 1:
            return sum(grid[0])

        cost_heap = []
        heapq.heappush(cost_heap, (grid[0][0], (0, 0)))
        visited = {(0, 0)}

        while cost_heap:
            curr = heapq.heappop(cost_heap)

            i, j = curr[1][0] - 1, curr[1][1]
            if indexValid(grid, i, j, visited):
                if i == len(grid) - 1 and j == len(grid[0]) - 1:
                    return grid[i][j] + curr[0]
                heapq.heappush(cost_heap, (grid[i][j] + curr[0], (i, j)))
                visited.add((i, j))

            i, j = curr[1][0] + 1, curr[1][1]
            if indexValid(grid, i, j, visited):
                if i == len(grid) - 1 and j == len(grid[0]) - 1:
                    return grid[i][j] + curr[0]
                heapq.heappush(cost_heap, (grid[i][j] + curr[0], (i, j)))
                visited.add((i, j))

            i, j = curr[1][0], curr[1][1] - 1
            if indexValid(grid, i, j, visited):
                if i == len(grid) - 1 and j == len(grid[0]) - 1:
                    return grid[i][j] + curr[0]
                heapq.heappush(cost_heap, (grid[i][j] + curr[0], (i, j)))
                visited.add((i, j))

            i, j = curr[1][0], curr[1][1] + 1
            if indexValid(grid, i, j, visited):
                if i == len(grid) - 1 and j == len(grid[0]) - 1:
                    return grid[i][j] + curr[0]
                heapq.heappush(cost_heap, (grid[i][j] + curr[0], (i, j)))
                visited.add((i, j))

            return -1
