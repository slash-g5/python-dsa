# User function Template for python3
# https://www.geeksforgeeks.org/problems/median-in-a-row-wise-sorted-matrix1527/1
import sys

class Solution:

    def get_min(self, matrix, R, C):
        ans = matrix[0][0]
        for i in range(R):
            ans = min(ans, matrix[i][0])
        return ans

    def get_max(self, matrix, R, C):
        ans = matrix[0][C - 1]
        for i in range(R):
            ans = max(ans, matrix[i][C - 1])
        return ans

    def row_grt_count(self, matrix, R, c_start, c_end, number):
        # get number of (elements >= number) where elements belong to matrix[R][c_start:c_end+1]
        if c_start == c_end:
            return 1 if matrix[R][c_start] >= number else 0
        if c_start > c_end:
            return 0
        c_mid = (c_start + c_end) // 2
        if matrix[R][c_mid] >= number:
            # this means c_mid, c_mid+1, ..., c_end all have > values
            return c_end - c_mid + 1 + self.row_grt_count(matrix, R, c_start, c_mid - 1, number)
        else:
            # this means c_start, c_start+1, ....., c_mid all have < values
            return self.row_grt_count(matrix, R, c_mid + 1, c_end, number)

    def find_nxt_grt_elem_row(self, matrix, r, c_start, c_end, elem):
        if c_end < c_start:
            return sys.maxsize
        if c_start == c_end:
            return matrix[r][c_start] if matrix[r][c_start] > elem else sys.maxsize
        c_mid = (c_start + c_end) // 2
        if matrix[r][c_mid] > elem:
            return self.find_nxt_grt_elem_row(matrix, r, c_start, c_mid, elem)
        return self.find_nxt_grt_elem_row(matrix, r, c_mid + 1, c_end, elem)

    def find_next_elem(self, matrix, R, C, elem):
        ans = self.get_max(matrix, R, C)
        for i in range(R):
            ans = min(ans, self.find_nxt_grt_elem_row(matrix, i, 0, C - 1, elem))
        return ans

    def median_helper(self, matrix, R, C, offset, curr_min, curr_max):
        if curr_min == curr_max:
            return curr_min
        if curr_min > curr_max:
            return 619
        mid = (curr_min + curr_max) // 2
        l_count = 0  # l_count = total enteries between curr_min and mid, including both
        for i in range(R):
            # first calculate elements strictly > mid
            row_grt_count_mid = self.row_grt_count(matrix, i, 0, C - 1, mid + 1)
            # calculate elements >= curr_min
            row_grt_count_min = self.row_grt_count(matrix, i, 0, C - 1, curr_min)
            l_count = l_count + row_grt_count_min - row_grt_count_mid
            if l_count > offset:
                break
        if l_count == offset:
            return self.find_next_elem(matrix, R, C, mid)
        if l_count > offset:
            return self.median_helper(matrix, R, C, offset, curr_min, mid)
        if l_count < offset:
            return self.median_helper(matrix, R, C, offset - l_count, mid + 1, curr_max)

    def median(self, matrix, R, C):
        # code here
        if R == 0 or C == 0:
            return -1
        if R == 1:
            return matrix[0][C // 2]
        return self.median_helper(matrix, R, C, (R * C) // 2, self.get_min(matrix, R, C), self.get_max(matrix, R, C))

if __name__ == '__main__':
    ob = Solution()
    r,c = map(int,input().strip().split())
    matrix = [[0 for j in range(c)] for i in range(r)]
    for i in range(r):
        t=[int(el) for el in input().split()]
        for j in range(c):
            matrix[i][j]=t[j]
    ans = ob.median(matrix, r, c)
    print(ans)
