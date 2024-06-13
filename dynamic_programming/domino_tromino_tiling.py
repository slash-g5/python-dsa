# https://leetcode.com/problems/domino-and-tromino-tiling/

class Solution:
    @staticmethod
    def numTilings(n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2

        dp_b_b = 1
        dp_b = 2

        be_b_b = 1
        be_b = 2

        for i in range(2, n):
            b_temp = be_b
            d_temp = dp_b
            dp_b = (dp_b + dp_b_b + 2 * be_b_b) % (10 ** 9 + 7)
            be_b = (be_b + d_temp) % (10 ** 9 + 7)
            dp_b_b = d_temp
            be_b_b = b_temp

        return dp_b
