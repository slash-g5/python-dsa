import heapq
import sys
from typing import List


class Solution:
    @staticmethod
    def reachableNodes(edges: List[List[int]], maxMoves: int, n: int) -> int:
        def getAdjList(edges, n):
            adj = [[] for _ in range(n)]
            for edge in edges:
                adj[edge[0]].append((edge[1], edge[2]))
                adj[edge[1]].append((edge[0], edge[2]))
            return adj

        dijQ = []
        heapq.heappush(dijQ, (0, 0))

        visited = {}
        adj = getAdjList(edges, n)

        dist = [sys.maxsize for _ in range(n)]
        dist[0] = 0

        ans = 0

        while dijQ:
            cost, curr_node = heapq.heappop(dijQ)
            if curr_node in visited:
                continue
            if cost > maxMoves:
                break
            visited[curr_node] = 1
            for elem in adj[curr_node]:
                if cost + elem[1] < maxMoves:
                    visited[(min(curr_node, elem[0]), max(curr_node, elem[0]))] = elem[1]
                else:
                    if (min(curr_node, elem[0]), max(curr_node, elem[0])) in visited:
                        visited[(min(curr_node, elem[0]), max(curr_node, elem[0]))] += maxMoves - cost
                        visited[(min(curr_node, elem[0]), max(curr_node, elem[0]))] = min(
                            visited[(min(curr_node, elem[0]), max(curr_node, elem[0]))], elem[1])
                    else:
                        visited[(min(curr_node, elem[0]), max(curr_node, elem[0]))] = maxMoves - cost
                if elem[0] in visited:
                    continue
                if dist[elem[0]] > cost + elem[1] + 1:
                    dist[elem[0]] = cost + elem[1] + 1
                    heapq.heappush(dijQ, (cost + elem[1] + 1, elem[0]))

        for key in visited:
            print(f'key = {key} value = {visited[key]}')
            ans += visited[key]

        return ans
