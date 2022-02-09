import collections


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
graph = collections.defaultdict(list, graph)


visited = set()


def dfs(visited, graph, node):
    if node not in visited:
        visited.add(node)
        print(node)
        for n in graph[node]:
            dfs(visited, graph, n)


dfs(visited, graph, "A")
