# User function Template for python3
# https://www.geeksforgeeks.org/problems/shortest-path-in-undirected-graph/1
from typing import List
from collections import deque


class Solution:
    def shortestPath(self, n: int, m: int, edges: List[List[int]]) -> List[int]:

        def update(v1, v2):
            if v2 == -1:
                return True
            return v2 > v1

        def dfs(adjList, start, visited, visitedNodes):
            if start in visited:
                return
            visited.add(start)
            for elem in adjList[start]:
                dfs(adjList, elem[0], visited, visitedNodes)
            visitedNodes.appendleft(start)

        def topSort(adjList, start=0):
            visitedNodes = deque()
            dfs(adjList, start, set(), visitedNodes)
            return visitedNodes

        def getAdjList(edges, n):
            ans = [[] for _ in range(n)]
            for edge in edges:
                ans[edge[0]].append((edge[1], edge[2]))
            return ans

        if n == 0:
            return []

        if n == 1:
            return [0]

        adjList = getAdjList(edges, n)
        tSort = list(topSort(adjList))

        # print(tSort)

        cost = [-1 for _ in range(n)]

        cost[0] = 0

        for node in tSort:
            for elem in adjList[node]:
                if update(cost[node] + elem[1], cost[elem[0]]):
                    cost[elem[0]] = cost[node] + elem[1]

        return cost