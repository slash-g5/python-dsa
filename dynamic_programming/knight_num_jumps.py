# https://leetcode.com/problems/knight-dialer/
class Solution:
    def knightDialer(self, n: int) -> int:
        def isValid(i, j):
            if i < 0 or j < 0 or i > 3 or j > 2:
                return False
            if i == 3 and (j == 0 or j == 2):
                return False
            return True

        kVect = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]
        dp = [[0 for _ in range(3)] for _ in range(4)]
        pre_dp = [[0 for _ in range(3)] for _ in range(4)]

        if n == 1:
            return 10

        for i in range(4):
            for j in range(3):
                if isValid(i, j):
                    dp[i][j] = 1
                    pre_dp[i][j] = 1

        curr = 2

        while curr <= n:
            for i in range(4):
                for j in range(3):
                    dp[i][j] = 0
                    if not isValid(i, j):
                        continue
                    for vect in kVect:
                        if isValid(i + vect[0], j + vect[1]):
                            dp[i][j] += pre_dp[i + vect[0]][j + vect[1]]
            for i in range(4):
                for j in range(3):
                    pre_dp[i][j] = dp[i][j] % (10 ** 9 + 7)
            curr += 1

        ans = 0

        for i in range(4):
            for j in range(3):
                if isValid(i, j):
                    ans += dp[i][j]
                    ans %= (10 ** 9 + 7)

        return ans
