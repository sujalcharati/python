 # here we select an element which is small and we swap it to the left most  index of  array 
def selection_sort(arr):
    for i in range(len(arr)):# i,j and min here represent index of array
        min = i
        for j in range(min+1,len(arr)):
            if arr[min]> arr[j]:
               min =j
        arr[i], arr[min]=arr[min], arr[i]# swaping of elements
    return arr 
array = [5,2,3,4,1]       
ans = selection_sort(array)# function call
print("sorted array:",ans)







        