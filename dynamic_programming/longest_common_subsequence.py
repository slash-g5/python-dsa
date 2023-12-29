class Solution:
    def longestCommonSubstr(self, S1, S2, n, m):
        # code here
        dp = [[-1 for _ in range(m)] for _ in range(n)]

        if S1[0] == S2[0]:
            dp[0][0] = 1
        else:
            dp[0][0] = 0

        for i in range(n):
            if S1[i] == S2[0]:
                dp[i][0] = 1
            else:
                dp[i][0] = 0

        for i in range(m):
            if S1[0] == S2[i]:
                dp[0][i] = 1
            else:
                dp[0][i] = 0

        for i in range(1, n):
            for j in range(1, m):
                if S1[i] == S2[j]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = 0

        max1 = 0
        for i in range(n):
            for j in range(m):
                max1 = max(max1, dp[i][j])

        return max1
    