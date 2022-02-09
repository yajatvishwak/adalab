graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'E'],
    'D': ['B', 'E', 'F'],
    'E': ['B', 'C', 'D', 'F'],
    'F': ['D', 'E']
}


visited = set()
queue = []


def bfs(node):
    visited.add(node)
    queue.append(node)

    while queue:
        s = queue.pop(0)
        print(s)
        for neig in graph[s]:
            if neig not in visited:
                visited.add(neig)
                queue.append(neig)


bfs("A")
