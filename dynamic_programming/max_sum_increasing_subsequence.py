class Solution:
    def maxSumIS(self, Arr, n):
        # code here
        if n == 0:
            return -1
        if n == 1:
            return Arr[0]
        dp = [-1 for _ in range(n)]
        dp[0] = Arr[0]
        for i in range(1, n):
            curr_max = Arr[i]
            for j in range(0, i):
                if Arr[j] < Arr[i]:
                    curr_max = max(dp[j] + Arr[i], curr_max)
            dp[i] = curr_max
        return max(dp)
