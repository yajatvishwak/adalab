import heapq
from pprint import pprint


graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
         [4, 0, 8, 0, 0, 0, 0, 11, 0],
         [0, 8, 0, 7, 0, 4, 0, 0, 2],
         [0, 0, 7, 0, 9, 14, 0, 0, 0],
         [0, 0, 0, 9, 0, 10, 0, 0, 0],
         [0, 0, 4, 14, 10, 0, 2, 0, 0],
         [0, 0, 0, 0, 0, 2, 0, 1, 6],
         [8, 11, 0, 0, 0, 0, 1, 0, 7],
         [0, 0, 2, 0, 0, 0, 6, 7, 0]]
N = 9

for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            graph[i][j] = float("inf")
adj = {i: [] for i in range(9)}
for i in range(9):
    for j in range(i+1, 9):
        adj[i].append((graph[i][j], j))
        adj[j].append((graph[i][j], i))

visited = set()
minH = [(0, 0)]  # cost , node to reach
totalcost = 0

while minH:
    cost, node = heapq.heappop(minH)
    if node in visited:
        continue
    visited.add(node)
    print("Visited", node, "cost from node", cost)
    totalcost = max(totalcost, cost)
    for neighCost, neigh in adj[node]:
        if neigh not in visited:
            heapq.heappush(minH, (neighCost+cost, neigh))

print(totalcost)
