def isSub(sum, arr, n):
    if sum == 0:
        return True
    if n == 0 and sum != 0:
        return False
    if arr[n-1] > sum:
        return isSub(sum, arr, n-1)
    return isSub(sum, arr, n-1) or isSub(sum-arr[n-1], arr, n-1)
