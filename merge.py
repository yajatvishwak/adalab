def merge(arr):
    if len(arr) > 1:
        left = arr[:len(arr)//2]
        right = arr[len(arr)//2:]
        merge(left)
        merge(right)
     
        i = 0
        j = 0
        k = 0
        while i< len(left) and j<len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i+=1
            else:
                arr[k] = right[j]
                j+=1
            k+=1
        
        while i< len(left):
            arr[k] = left[i]
            i+=1
            k+=1
        while j< len(right):
            arr[k] = right[j]
            j+=1
            k+=1

arr = [8,4,2,1,5,6]
merge(arr)
print(arr)