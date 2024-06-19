def quick_sort(arr):
    if len(arr) < 2:
        return arr
    mid= len(arr)//2
    piv = arr[0]
    left=[]
    right=[]
    for i in (arr[1:]):
        if i<= piv:
            left.append(i)
        else:
            right.append(i)
    return quick_sort(left)+[piv]+quick_sort(right)
arr = [8,4,2,3,7,-1,6,78,54,3,2]
print(quick_sort(arr))