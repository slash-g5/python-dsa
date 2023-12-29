from collections import deque


my_graph = {
    'a': ['b', 'c'],
    'b': ['d', 'a'],
    'c': ['e'],
    'd': ['f'],
    'e': ['a'],
    'f': ['b']
}


def bfs(graph, node):
    my_queue = deque()
    is_visited = set()
    if not graph or not graph[node]:
        return []
    ans = []
    my_queue.append(node)
    while my_queue:
        curr = my_queue.popleft()
        is_visited.add(curr)
        if len(graph[curr]) > 0:
            for n in graph[curr]:
                if n not in is_visited:
                    my_queue.append(n)
        ans.append(curr)
    return ans


if __name__ == "__main__":
    print(bfs(my_graph, 'f'))
