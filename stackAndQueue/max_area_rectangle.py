# https://leetcode.com/problems/maximal-rectangle/
from typing import List
class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        def constructHistMat(matrix, r, c):
            ans = [[0 for _ in range(c)] for _ in range(r)]
            for i in range(c):
                ans[0][i] = int(matrix[0][i])
            for i in range(1, r):
                for j in range(c):
                    if matrix[i][j] == '0':
                        ans[i][j] = 0
                        continue
                    ans[i][j] = ans[i - 1][j] + 1
            return ans

        def maxHistArea(arr, n):
            if n == 0:
                return 0
            next_small = [n for _ in range(n)]
            prev_small = [-1 for _ in range(n)]
            stack = []
            stack.append(0)
            for i in range(1, n):
                while stack and arr[stack[-1]] >= arr[i]:
                    stack.pop()
                if stack:
                    prev_small[i] = stack[-1]
                stack.append(i)
            stack = []
            for i in range(n - 1, -1, -1):
                while stack and arr[stack[-1]] >= arr[i]:
                    stack.pop()
                if stack:
                    next_small[i] = stack[-1]
                stack.append(i)
            max_area = 0
            for i in range(n):
                max_area = max(arr[i] * (next_small[i] - prev_small[i] - 1), max_area)
            return max_area

        r = len(matrix)
        c = len(matrix[0])
        hist_mat = constructHistMat(matrix, r, c)

        final_ans = 0

        for i in range(r):
            final_ans = max(final_ans, maxHistArea(hist_mat[i], c))

        return final_ans

