 
def selection_sort(arr):
    for i in range(len(arr)):
        min = i
        for j in range(min+1,len(arr)):
            if arr[min]> arr[j]:
               min =j
        arr[i], arr[min]=arr[min], arr[i]
    return arr 
array = [5,2,3,4,1]       
ans = selection_sort(array)
print("sorted array:",ans)







        