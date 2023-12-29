# problem link https://practice.geeksforgeeks.org/problems/peak-element/1?page=2&sortBy=submissions
class Solution:

    def helper_func(self, arr, start, end):
        n = end - start + 1
        if n < 1:
            return -1
        if n < 2:
            return start
        if arr[end] >= arr[end - 1]:
            return end
        mid = start + n // 2
        if arr[mid + 1] <= arr[mid] and arr[mid - 1] <= arr[mid]:
            return mid
        if arr[mid] < arr[mid - 1]:
            return self.helper_func(arr, start, mid - 1)
        return self.helper_func(arr, mid + 1, end)

    def peak_element(self, arr, n):
        return self.helper_func(arr, 0, n - 1)
