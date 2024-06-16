def binary(arr,left,right,x):
     while right>=left:
          mid = left + (right -left)//2
          if arr[mid] ==x:
               return mid
          elif arr[mid] > x:
               return binary(arr,left,mid-1,x)
          else:
               return binary(arr,mid+1,right,x)
     return -1
arr = [2,3,4,5,6,7]
x=5
ans = binary(arr,0,len(arr)-1,x)
if ans != -1:
 print('the element is found at index',ans)
else:
     print("the element is not found" )

          