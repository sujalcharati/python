arr = [12, 11, 13, 5, 6, 7]
def buildMaxHeap(arr):
    for i in range(len(arr)//2-1, -1):
        maxHeapify(arr, i)