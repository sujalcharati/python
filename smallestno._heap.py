import heapq

def kth_smallest(nums, k):
    heapq.heapify(nums)


    for _ in range(k):
        result = heapq.heappop(nums)

    return result


arr = [7, 4 , 6 , 3 , 9 , 1]
k = 2
print(f"The {k}th smallest element in the array is:", kth_smallest(arr, k))