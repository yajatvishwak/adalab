def nQueens(n):
    if n < 3:
        return []
    col = set()
    pos = set()
    neg = set()
    res = []
    board = [["."]*n for i in range(n)]

    def backtrack(r):
        if r == n:
            res.append(["".join(row) for row in board])
            return
        for c in range(n):
            if c in col or (r+c) in pos or (r-c) in neg:
                continue
            col.add(c)
            pos.add(r+c)
            neg.add(r-c)
            board[r][c] = "Q"
            backtrack(r+1)
            col.remove(c)
            pos.remove(r+c)
            neg.remove(r-c)
            board[r][c] = "."

    backtrack(0)
    return res


print(nQueens(4))
