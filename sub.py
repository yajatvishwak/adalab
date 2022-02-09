v = set()


def sub(arr, sum,  n):
    if sum == 0:
        return True
    if n == 0 and sum != 0:
        return False
    if arr[n-1] > sum:
        return sub(arr, sum, n-1)
    return sub(arr, sum, n-1) or sub(arr, sum - arr[n-1], n-1)


print(sub([7, 3, 1, 5, 3], 6, 5))
print(v)
