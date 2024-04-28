# https://www.geeksforgeeks.org/problems/topological-sort/1
class Solution:

    # Function to return list containing vertices in Topological order.

    def topdfs(self, curr, adj, not_visited, ans):
        if curr not in not_visited:
            return
        for elem in adj[curr]:
            self.topdfs(elem, adj, not_visited, ans)
        ans.append(curr)
        not_visited.discard(curr)

    def topoSort(self, V, adj):
        # Code here
        # 0 3 1 2 5 4
        ans = []
        not_visited = {i for i in range(V)}
        while not_visited:
            temp_ans = []
            self.topdfs(next(iter(not_visited)), adj, not_visited, temp_ans)
            ans.extend(temp_ans)
        return ans[::-1]
