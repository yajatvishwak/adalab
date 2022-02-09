def bc(n,c):
    if n==c or c==0:
        return 1
    return bc(n-1, c-1) + bc(n-1, c)

print(bc(7,6))