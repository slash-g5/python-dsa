# https://www.geeksforgeeks.org/problems/search-in-a-matrix-1587115621/1
class Solution:

    # Function to search a given number in row-column sorted matrix.

    @staticmethod
    def search(matrix, n, m, x):
        # code here
        curr = (0, m - 1)
        while True:
            if curr[0] >= n or curr[1] >= m:
                return False
            if curr[0] < 0 or curr[1] < 0:
                return False
            if matrix[curr[0]][curr[1]] == x:
                return True
            if matrix[curr[0]][curr[1]] == x:
                return True
            if matrix[curr[0]][curr[1]] > x:
                curr = (curr[0], curr[1] - 1)
                continue
            if matrix[curr[0]][curr[1]] < x:
                curr = (curr[0] + 1, curr[1])
                continue
