# https://practice.geeksforgeeks.org/problems/merge-two-sorted-arrays-1587115620/1?page=3&sprint=a663236c31453b969852f9ea22507634&sprint=a663236c31453b969852f9ea22507634&sortBy=difficulty
# https://www.geeksforgeeks.org/merge-two-sorted-arrays-o1-extra-space/
def findKthElement(arr1, arr2, l1, l2, k):
    if l1 >= len(arr1):
        return arr2[l2 + k]
    if l2 >= len(arr2):
        return arr1[l1 + k]
    if k == 0:
        return min(arr1[l1], arr2[l2])
    if k % 2 == 1:
        mid = k // 2
    else:
        mid = k // 2 - 1

    mid2 = min(len(arr2) - 1, l2 + mid)
    mid1 = min(len(arr1) - 1, l1 + mid)

    if arr1[mid1] > arr2[mid2]:
        return findKthElement(arr1, arr2, l1, mid2 + 1, k - mid2 + l2 - 1)
    return findKthElement(arr1, arr2, mid1 + 1, l2, k - mid1 + l1 - 1)


class Solution:

    # Function to merge the arrays.
    def merge(self, arr1, arr2, n, m):
        # code here
        nth_element = findKthElement(arr1, arr2, 0, 0, n)
        i1 = n - 1
        i2 = 0
        while True:
            if i1 < 0 or i2 >= m:
                break
            if arr1[i1] >= nth_element >= arr2[i2]:
                arr1[i1], arr2[i2] = arr2[i2], arr1[i1]
                i1 -= 1
                i2 += 1
                continue
            else:
                break
        arr1.sort()
        arr2.sort()
