import heapq
import sys

def kthSmallest(self, arr, l, r, k):
    '''
    arr : given array
    l : starting index of the array i.e 0
    r : ending index of the array i.e size-1
    k : find kth smallest element and return using this function
    '''
    if l > r:
        return -sys.maxsize
    if k > r - l + 1:
        return -sys.maxsize
    min_heap = []
    for i in range(k):
        heapq.heappush(min_heap, -arr[i])
    for i in range(k, r + 1):
        if arr[i] < -min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, -arr[i])
    return -min_heap[0]
