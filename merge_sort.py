def merge_sort(arr1,arr2):
    i=0
    j=0
    arr3=[]
    while i< len(arr1) and j < len(arr):
          if arr1[i]< arr2[j]:
             arr3[i]= arr1[i]
             i+=1
          else:
             arr3[i]= arr2[j]
             j+=1
    while i<len(arr1):
        arr3[i]= arr1[i]
        i+=1
        




            


