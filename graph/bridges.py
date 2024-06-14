# https://leetcode.com/problems/critical-connections-in-a-network/

import sys
from typing import List

ids = []
low_link = []
visited = []
id = 0


class Solution:

    @staticmethod
    def criticalConnections(n: int, connections: List[List[int]]) -> List[List[int]]:

        global ids, low_link, visited, id

        ids = [-1 for _ in range(n)]
        low_link = [sys.maxsize for _ in range(n)]
        visited = [False for _ in range(n)]

        def dfs(start, prev, bridges, adj):
            global ids, low_link, visited, id

            if visited[start]:
                return
            visited[start] = True

            ids[start] = id
            low_link[start] = id
            id += 1

            for next_node in adj[start]:
                if next_node == prev:
                    continue
                dfs(next_node, start, bridges, adj)
                low_link[start] = min(low_link[start], low_link[next_node])

            if prev != -1 and low_link[start] > ids[prev]:
                bridges.append((prev, start))

        def getAdj(connections, n):
            adj = [[] for _ in range(n)]
            for i, j in connections:
                adj[i].append(j)
                adj[j].append(i)
            return adj

        adj = getAdj(connections, n)

        bridges = []
        for i in range(n):
            if visited[i]:
                continue
            dfs(i, -1, bridges, adj)

        return bridges
