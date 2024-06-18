from typing import List
import heapq


class Solution:
    @staticmethod
    def minCost(grid: List[List[int]]) -> int:
        # 1 -> right
        # 2 -> left
        # 3 -> down
        # 4 -> up

        def isValid(i, j, m, n):
            return (0 <= i < m) and (0 <= j < n)

        def createAdj(grid, m, n):
            adj = {}
            trans = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for i in range(m):
                for j in range(n):
                    for k in range(1, 5):
                        if isValid(i + trans[k - 1][0], j + trans[k - 1][1], m, n):
                            value = 0
                            if grid[i][j] != k:
                                value += 1
                            if (i, j) in adj:
                                adj[(i, j)].append(((i + trans[k - 1][0], j + trans[k - 1][1]), value))
                            else:
                                adj[(i, j)] = [((i + trans[k - 1][0], j + trans[k - 1][1]), value)]

            return adj

        m = len(grid)
        n = len(grid[0])

        adj = createAdj(grid, m, n)

        print(adj)

        heap = []
        heapq.heappush(heap, (0, (0, 0)))

        dist = {(0, 0): 0}
        visited = set()

        while heap:
            cost, curr = heapq.heappop(heap)
            if curr in visited:
                continue
            if curr == (m - 1, n - 1):
                return dist[curr]

            for elem in adj[curr]:
                if elem[0] in visited:
                    continue
                if elem[0] not in dist or elem[1] + cost < dist[elem[0]]:
                    dist[elem[0]] = elem[1] + cost
                    heapq.heappush(heap, (dist[elem[0]], elem[0]))

        return -1
