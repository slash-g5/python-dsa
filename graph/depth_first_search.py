from collections import deque


my_graph = {
    'a': ['b', 'c'],
    'b': ['d'],
    'c': ['e'],
    'd': ['f'],
    'e': [],
    'f': []
}


def dfs(graph, node):
    stack = deque()
    ans = []
    if not graph or not graph[node]:
        return []
    stack.append(node)
    while stack:
        curr = stack.pop()
        ans.append(curr)
        if len(graph[curr]) > 0:
            for i in range(len(graph[curr])-1, -1, -1):
                stack.append(graph[curr][i])
    return ans


if __name__ == "__main__":
    print(dfs(my_graph, 'a'))
