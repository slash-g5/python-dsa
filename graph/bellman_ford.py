# User function Template for python3
# https://www.geeksforgeeks.org/problems/distance-from-the-source-bellman-ford-algorithm/1

class Solution:
    # Function to construct and return cost of MST for a graph
    # represented using adjacency matrix representation
    '''
    V: nodes in graph
    edges: adjacency list for the graph
    S: Source
    '''

    def bellman_ford(self, V, edges, S):
        # code here
        if V == 0:
            return []
        if V == 1:
            return [0]

        dist = [10 ** 8 for _ in range(V)]
        dist[S] = 0

        for i in range(V - 1):
            for edge in edges:
                if dist[edge[0]] == 10 ** 8:
                    continue
                if dist[edge[0]] + edge[2] < dist[edge[1]]:
                    dist[edge[1]] = dist[edge[0]] + edge[2]

        for edge in edges:
            if dist[edge[0]] == 10 ** 8:
                continue
            if dist[edge[0]] + edge[2] < dist[edge[1]]:
                return [-1]

        return dist

