# User function Template for python3

class Solution:

    # Function to find number of strongly connected components in the graph.
    def reverseEdges(self, adj):
        adj_rv = [[] for _ in range(len(adj))]
        for i in range(len(adj)):
            for it in adj[i]:
                adj_rv[it].append(i)
        return adj_rv

    def dfs1(self, curr, adj, visited, v_stack, total):
        if curr not in total:
            return
        if curr in visited:
            return
        visited.add(curr)
        for elem in adj[curr]:
            self.dfs1(elem, adj, visited, v_stack, total)
        v_stack.append(curr)

    def kosaraju(self, V, adj):
        # code here
        not_visited_1 = {i for i in range(V)}

        adj_rv = self.reverseEdges(adj)

        count = 0

        while not_visited_1:

            curr = next(iter(not_visited_1))

            v_stack = []
            c_visited = set()
            self.dfs1(curr, adj, c_visited, v_stack, not_visited_1)

            not_visited_1 = not_visited_1 - c_visited

            while c_visited and v_stack:
                curr = v_stack[len(v_stack) - 1]
                if curr not in c_visited:
                    v_stack.pop()
                    continue
                count += 1
                visited = set()
                self.dfs1(curr, adj_rv, visited, [], c_visited)
                if not visited:
                    break
                c_visited = c_visited - visited

        print(not_visited_1)

        return count


# {
# Driver Code Starts
# Initial Template for Python 3

import sys

sys.setrecursionlimit(10 ** 6)
if __name__ == '__main__':
    V, E = list(map(int, input().strip().split()))
    adj = [[] for i in range(V)]
    for i in range(E):
        a, b = map(int, input().strip().split())
        adj[a].append(b)
    ob = Solution()

    print(ob.kosaraju(V, adj))
