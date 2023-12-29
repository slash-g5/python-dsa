# User function Template for python3

def helper(matrix, i, j, diff_x_max, diff_y_max):
    ans = []
    for i1 in range(i, i + diff_x_max + 1):
        ans.append(matrix[i1][j])
    for j1 in range(j + 1, j + diff_y_max + 1):
        ans.append(matrix[i + diff_x_max][j1])
    for i1 in range(i + diff_x_max - 1, i - 1, -1):
        ans.append(matrix[i1][j + diff_y_max])
    for j1 in range(j + diff_y_max - 1, j, -1):
        ans.append(matrix[i][j1])
    return ans


class Solution:

    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, matrix, r, c):
        # code here
        ans = []
        num_iterations = min(r, c) // 2 + min(r, c) % 2
        i1, j1 = 0, 0
        for i in range(num_iterations):
            ans.extend(helper(matrix, i1, j1, c - 1 - 2 * num_iterations, r - 1 - 2 * num_iterations))
            i1 += 1
            j1 += 1
        return ans


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        r,c = map(int, input().strip().split())
        values = list(map(int, input().strip().split()))
        k = 0
        matrix =[]
        for i in range(r):
            row=[]
            for j in range(c):
                row.append(values[k])
                k+=1
            matrix.append(row)
        obj = Solution()
        ans = obj.spirallyTraverse(matrix,r,c)
        for i in ans:
            print(i,end=" ")
        print()
