# User function Template for python3
# https://www.geeksforgeeks.org/problems/shortest-source-to-destination-path3544/1
from collections import deque


class Solution:

    def mat_bfs(self, mat, sX, sY, eX, eY):

        def indexValid(mat, x, y, visited):
            if (x, y) in visited:
                return False
            if x < 0 or y < 0:
                return False
            if x >= len(mat) or y >= len(mat[0]):
                return False
            return True if mat[x][y] == 1 else 0

        if sX == eX and sY == eY:
            return 0

        if mat[sX][sY] == 0:
            return -1

        bfsQ = deque()
        visited = set()
        bfsQ.append((sX, sY))

        count = -1

        while bfsQ:
            count += 1
            tempQ = deque()
            while bfsQ:
                curr = bfsQ.popleft()
                if curr in visited:
                    continue
                visited.add(curr)
                if curr[0] == eX and curr[1] == eY:
                    return count

                if indexValid(mat, curr[0] - 1, curr[1], visited):
                    tempQ.append((curr[0] - 1, curr[1]))

                if indexValid(mat, curr[0] + 1, curr[1], visited):
                    tempQ.append((curr[0] + 1, curr[1]))

                if indexValid(mat, curr[0], curr[1] + 1, visited):
                    tempQ.append((curr[0], curr[1] + 1))

                if indexValid(mat, curr[0], curr[1] - 1, visited):
                    tempQ.append((curr[0], curr[1] - 1))
            bfsQ = tempQ

        return -1

    def shortestDistance(self, N, M, A, X, Y):
        # code here
        return self.mat_bfs(A, 0, 0, X, Y)
