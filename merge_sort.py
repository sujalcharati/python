def merge_sort(arr1,arr2):
    i=0 #indices
    j=0
    arr3=[]
    while i< len(arr1) and j < len(arr2):
          if arr1[i]< arr2[j]:
             arr3[i]= arr1[i]# initialization
             i+=1
          else:
             arr3[i]= arr2[j]
             j+=1
    while i<len(arr1):
        arr3[i]= arr1[i]
        i+=1
    while j<len(arr2):
        arr3[i]= arr2[i]
        j+=1
def merge_fxn(arr3):
    if len(arr3)<2:
        return arr3
    mid= len(arr3)//2
    arr1,arr2 =None,None
    arr1 = merge_fxn(arr3[:mid])# traverse elements from starting index to middle index 
    arr2 = merge_fxn(arr3[mid:])# traverse elements from middle index to last index 
    return merge_sort(arr1,arr2)
arr3=[1,2,3,4,5,6,7,8,9,10]

print(merge_fxn(arr3))


       
        




            


