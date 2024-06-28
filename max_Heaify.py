arr = [12, 11, 13, 5, 6, 7]
def maxHeapify(arr, i):
  largest = i
  l= 2*i+1 #left array of subtree
  r= 2*i+2 #right array of subtree


  if l < len(arr) and arr[l] > arr[largest]:
      largest = l
    
  if r < len(arr) and arr[r] > arr[largest]:
     largest = r
  if largest != i:
        arr[i],arr[largest]= arr[largest],arr[i]
        maxHeapify(arr, largest)
print(arr) 



