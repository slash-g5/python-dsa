# https://practice.geeksforgeeks.org/problems/inversion-of-array-1587115620/1?page=1&sortBy=submissions
class Solution:
    # User function Template for python3

    # arr[]: Input Array
    # N : Size of the Array arr[]
    # Function to count inversions in the array.
    def inversionCount(self, arr, n):
        # Your Code Here
        def inversionCountHelper(arr, start, end):
            if end <= start:
                return 0
            if end == start + 1:
                if arr[start] > arr[start + 1]:
                    arr[start], arr[start + 1] = arr[start + 1], arr[start]
                    return 1
                return 0
            mid = start + (end - start + 1) // 2
            left_count = inversionCountHelper(arr, start, mid)
            right_count = inversionCountHelper(arr, mid + 1, end)
            merge_count = 0
            i, j = start, mid + 1
            merge_array = []
            while i <= mid or j <= end:
                if i <= mid and j <= end:
                    if arr[i] <= arr[j]:
                        merge_array.append(arr[i])
                        i += 1
                    else:
                        merge_array.append(arr[j])
                        merge_count += mid - start + 1 - i + start
                        j += 1
                    continue
                if i <= mid:
                    merge_array.append(arr[i])
                    i += 1
                    continue
                if j <= end:
                    merge_array.append(arr[j])
                    j += 1
                    continue

            for i in range(start, end + 1):
                arr[i] = merge_array[i - start]

            return left_count + right_count + merge_count

        return inversionCountHelper(arr, 0, n - 1)
