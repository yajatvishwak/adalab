def bc(n, k):
    if k == 0 or n == k:
        return 1
    return bc(n-1, k-1) + bc(n-1, k)


print(bc(10, 6))
