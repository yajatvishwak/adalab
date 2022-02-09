

def topo(arr):
    allNode = set()
    for i, j in arr:
        allNode.add(i)
        allNode.add(j)

    while arr:
        n = getLeastIndegree(arr)
        print(n)
        allNode.remove(n)
        arr = removeNode(arr, n)

    for i in list(allNode):
        print(i)


def getLeastIndegree(arr):
    allNode = set()

    for i, j in arr:
        allNode.add(i)
        allNode.add(j)

    f = {i: 0 for i in list(allNode)}
    # print(list(allNode))
    for i, j in list(arr):
        f[j] += 1
    # print(f)
    #{1:0, 2:1, 3:1, 4:2, 5:1, 6:2}
    return min(f, key=f.get)


def removeNode(arr, n):
    res = []
    for i, j in arr:
        if i == n:
            continue
        res.append((i, j))
    return res


arr = [(1, 2),
       (1, 3),
       (2, 4),
       (2, 5),
       (3, 4),
       (3, 6),
       (4, 6)]

topo(arr)
