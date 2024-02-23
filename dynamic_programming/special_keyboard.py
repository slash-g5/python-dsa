# https://www.geeksforgeeks.org/problems/special-keyboard3018/1

class Solution:
    def optimalKeys(self, N):
        # code here

        dp = [i for i in range(N + 1)]

        for i in range(7, N + 1):

            for j in range(i - 2, 0, - 1):
                curr = (i - j - 1) * dp[j]
                dp[i] = max(curr, dp[i])

        return dp[N]
