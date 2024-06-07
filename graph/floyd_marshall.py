# https://www.geeksforgeeks.org/problems/implementing-floyd-warshall2042/1
class Solution:
    @staticmethod
    def shortest_distance(matrix):
        # Code here
        n = len(matrix)

        if n == 0:
            return

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if i == j or i == k or j == k:
                        continue
                    if matrix[k][j] == -1:
                        continue
                    if matrix[i][k] == -1:
                        continue
                    if matrix[i][j] == -1 or matrix[i][j] > matrix[i][k] + matrix[k][j]:
                        matrix[i][j] = matrix[i][k] + matrix[k][j]
