
import heapq
from pprint import pprint


G = [[0, 9, 75, 0, 0],
     [9, 0, 95, 19, 42],
     [75, 95, 0, 51, 66],
     [0, 19, 51, 0, 31],
     [0, 42, 66, 31, 0]]

inf = float("inf")

for i in range(5):
    for j in range(5):
        if G[i][j] == 0:
            G[i][j] = inf


adj = {i: [] for i in range(5)}

print(adj)
for i in range(5):
    for j in range(5):
        adj[i].append((G[i][j], i, j))
        #adj[j].append((G[i][j], j, i))

pprint(adj)
path = []
# prims
visited = set()
minH = [(0, 0, 0)]  # cost, from , to
totalCost = 0
while len(visited) < 5:
    cost, fromnode, node = heapq.heappop(minH)  # min from first
    if node in visited:
        continue
    visited.add(node)
    print("visiting", node, "from", fromnode, "at cost", cost)
    path.append((fromnode, node))
    totalCost += cost
    # extra step
    for nc, fromnodee, nn in adj[node]:
        if nn not in visited:
            heapq.heappush(minH, (nc, fromnodee, nn))

print(path)
