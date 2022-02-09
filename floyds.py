
from pprint import pprint


M = float("inf")
adj = [
    [0, M, 3, M],
    [2, 0, M, M],
    [M, 7, 0, 1],
    [6, M, M, 0]
]

for k in range(4):
    for i in range(4):
        for j in range(4):
            if adj[i][k] + adj[k][j] < adj[i][j]:
                adj[i][j] = adj[i][k] + adj[k][j]
for i in adj:
    print(i)
