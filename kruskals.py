
import heapq

INF = float('inf')
G = [[INF, 2, INF, 6, INF],
     [2, INF, 3, 8, 5],
     [INF, 3, INF, INF, 7],
     [6, 8, INF, INF, 9],
     [INF, 5, 7, 9, INF]]

for i in range(5):
    for j in range(5):
        if G[i][j] == 0:
            G[i][j] = 999
adj = {i: [] for i in range(5)}
lower = []
for i in range(5):
    for j in range(i+1, 5):
        adj[i].append((G[i][j], i, j))
        adj[j].append((G[i][j], j, i))
        lower.append((G[i][j], j, i))
        lower.append((G[i][j], i, j))


# kruskals
visited = set()
c, f, n = heapq.heappop(lower)

minH = [(0, f, n)]
totalCost = 0
while len(visited) < 5:
    cost, fromnode, node = heapq.heappop(minH)
    if node in visited:
        continue
    visited.add(node)
    print(visited)
    print("visiting", node, fromnode, "at cost", cost)
    totalCost += cost
    for nc, fromnodee, nn in adj[node]:
        if nn not in visited:
            heapq.heappush(minH, (nc, fromnodee, nn))

print(totalCost)
