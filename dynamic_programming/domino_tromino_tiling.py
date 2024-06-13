# https://leetcode.com/problems/domino-and-tromino-tiling/

# # Intuition and Approach
#
# This is a DP based solution of the problem.
#
# Why DP? We need to count number of tilings for a given number. We have a 2*n grid. If we start from the leftmost
# column we have few options to start tiling.
#
# Variables used:
# dp[i] => number of tilings possible for 2*i grid
# be[i] => number of tilings possible for 2*i grid with one extra column to the left having only one row.
#
# Note: Notice although the extra column can be in either first or second row of grid, we have not created two
# variables for   be[i], as both values will always be same due to symmetry.
#
# 1. we can either assign a 'vertical domino' to it. after that we would have to do tiling of remaining (n-1)
# columns. Therefore we can say in this approach we will have dp[n-1] solutions. 2. We can assign two 'horizontal
# dominos to start the tiling process. This will occupy two leftmost column and we would further need to do tiling
# for remaining (n-2) columns. Therefore this approach will give dp[n-2] solutions. 3. We can assign 'Tromino' to the
# leftmost columns. The leftmost column will be occupied by the tromino and additionally one of the cells in
# second-leftmost column will also be occupied depending on rotation of tromino. This means we will have be[n-2]
# further solutions for each case of rotation. Hence overall we will have 2*be[n-2] solutions for this case
#
# Considering the last point, we also need to keep adding values to the 'be' array. Similar to what we did for 'dp'
# array we can consider a grid 2*n dimension but additionally having one extra cell on the left. We have two ways to
# fill leftmost tile
#
# 4.1 Start with tromino, this will leave dp[n-1] options to fill the remaining cells.
# 4.2 Start with 'horizontal domino' this will leave be[n-1] further options.
#
# Hence based on all the above points we can say:
# 1. dp[i] = dp[i-1] + dp[i-2] + 2*be[n-2]
# 2. be[i] = be[i-1] + dp[i-1]
#
# As with any DP solution we can loop through values of i and fill up all elements in dp and be arrays, at the end we
# return dp[n] (or dp[n-1] for 0 based index).
#
# We can see dp[i] and be[i] only depend on last two values. Therefore instead of arrays be and dp we can define four
# variables for storing last two values of both dp and be arrays. This will reduce space complexity (refer code).

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
