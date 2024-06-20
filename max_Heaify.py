arr = [12, 11, 13, 5, 6, 7]
def maxHeapify(arr, i):

  l= 2*i+1
  r= (i*2)+2


  if l < len(arr) and arr[l] > arr[i]:
      largest = l
  else:
     largest = i
  if r < len(arr) and arr[r] > arr[largest]:
     largest = r
     if largest != i:
        arr[largest]= arr[i]
     val = maxHeapify(arr, largest)
     print(val)



