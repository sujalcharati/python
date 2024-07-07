 # question related to minimum number of jumps we take to reach the final step
arr = [2,3,1,4,3,1,2]
def jump(arr):
  n  = len(arr)
  ans =[float('inf')]*n# infinity
  ans[0]=0
  for i in range(n-1):
    for j in range (1,arr[i]+1):
        if i+j < n:
            ans[i+j]= min(ans[i+j],1+ ans[i])
  return (ans)
print (jump(arr))