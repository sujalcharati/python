def linear(arr,l,x):
    for i in range(l):
      if (arr[i]==x):
        return i
    return -1
arr = [1,2,3,4,5]
x= 3
l = len(arr)
res = linear(arr,l,x)

if res == -1:
   print("the element is not found")
else:
   print("the element is found at index",res)



