# User function Template for python3
# https://www.geeksforgeeks.org/problems/rotate-matrix-elements-clockwise2336/1

class Solution:
    def rotateMatrix(self, M, N, Mat):
        # code here
        # 1 2 3
        # 4 5 6
        # 7 8 9

        # temp = 1
        # 4 2 3
        # 4 5 6
        # 7 8 9

        # 9 9 9 9 9
        # 9 9 9 9 9
        # 9 9 9 9 9
        # 9 9 9 9 9
        # 9 9 9 9 9
        # 9 9 9 9 9

        curr_depth = 0
        max_depth = min(M, N) // 2

        while curr_depth < max_depth:
            final = (curr_depth + 1, curr_depth)
            temp = Mat[final[0]][final[1]]
            start = (curr_depth, curr_depth)
            while True:
                Mat[start[0]][start[1]], temp = temp, Mat[start[0]][start[1]]
                if start[0] == final[0] and start[1] == final[1]:
                    break
                if start[0] == curr_depth:
                    if start[1] == N - 1 - curr_depth:
                        start = (start[0] + 1, start[1])
                        continue
                    start = (start[0], start[1] + 1)
                    continue
                if start[0] == M - 1 - curr_depth:
                    if start[1] == curr_depth:
                        start = (start[0] - 1, start[1])
                        continue
                    start = (start[0], start[1] - 1)
                    continue
                if start[1] == curr_depth:
                    start = (start[0] - 1, start[1])
                    continue
                else:
                    start = (start[0] + 1, start[1])
            curr_depth += 1
        return Mat
