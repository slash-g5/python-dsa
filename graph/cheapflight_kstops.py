# https://leetcode.com/problems/cheapest-flights-within-k-stops/

from typing import List
from collections import deque
import sys


class Solution:
    @staticmethod
    def findCheapestPrice(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        def getAdjList(flights, n):
            adj = [[] for _ in range(n)]
            for flight in flights:
                adj[flight[0]].append((flight[1], flight[2]))
            return adj

        dist = [sys.maxsize for _ in range(n)]
        dist[src] = 0
        bfs_q = deque()
        adj = getAdjList(flights, n)
        bfs_q.append((0, src, 0))

        while bfs_q:
            curr = bfs_q.popleft()
            if curr[2] > k + 1:
                continue
            for next_node in adj[curr[1]]:
                if curr[0] + next_node[1] < dist[next_node[0]] and curr[2] <= k:
                    dist[next_node[0]] = curr[0] + next_node[1]
                    bfs_q.append((curr[0] + next_node[1], next_node[0], curr[2] + 1))

        if dist[dst] == sys.maxsize:
            return -1
        return dist[dst]
