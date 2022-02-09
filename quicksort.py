from turtle import right


def quick(arr):
    
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()
    
    g = []
    l = []
    for item in arr:
        if item < pivot:
            l.append(item)
        else:
            g.append(item)
    return quick(l) + [pivot] + quick(g)



print(quick([112,4,42,41]))