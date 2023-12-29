# https://practice.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1?page=2&sortBy=submissions
from typing import List
from collections import deque


def get_not_visited(visited, num_nodes):
    for i in range(num_nodes):
        if i not in visited:
            return i
    return -1


class Solution:
    # Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        # Code here
        if not adj:
            return False

        curr_start = 0
        visited = set()
        while curr_start >= 0:
            stack = deque()
            stack.append(curr_start)
            while stack:
                curr = stack.pop()
                if curr in visited:
                    return True
                visited.add(curr)
                for node in adj[curr]:
                    if node not in visited:
                        stack.append(node)

            curr_start = get_not_visited(visited, V)
        return False
