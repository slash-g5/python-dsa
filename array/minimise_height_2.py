# https://practice.geeksforgeeks.org/problems/minimize-the-heights3351/1?page=1&sprint=a663236c31453b969852f9ea22507634&sprint=a663236c31453b969852f9ea22507634&sortBy=submissions

class Solution:
    def getMinDiff(self, arr, n, k):
        # code here
        arr.sort()
        ans = arr[n-1] - arr[0]
        for i in range(n-1):
            if arr[i+1] < k:
                continue
            max1 = max(arr[n-1] - k, arr[i] + k)
            min1 = min(arr[0] + k, arr[i+1] - k)
            new_ans = max1 - min1
            if new_ans < ans:
                ans = new_ans
        return ans
