# User function Template for python3
# https://practice.geeksforgeeks.org/problems/minimum-number-of-jumps-1587115620/1?page=1&sortBy=submissions
# code using bfs, not most optimised
def minJumpsHelper(arr, n):
    if n == 0:
        return 0
    if arr[0] == 0:
        return -1
    visited = set()
    visited.add(0)
    curr_indexes = [0]
    height = 0
    while curr_indexes:
        new_indexes = []
        for index in curr_indexes:
            if (index + arr[index]) >= n - 1:
                return height + 1
            for i in range(index + 1, index + arr[index] + 1):
                if i > n - 1:
                    break
                if i not in visited:
                    if i == n - 1:
                        return height + 1
                    visited.add(i)
                    new_indexes.append(i)
        curr_indexes = new_indexes
        height += 1
    return -1


class Solution:
    def minJumps(self, arr, n):
        if n == 0:
            return 0

        if arr[0] == 0:
            return -1
        reach = arr[0]
        if reach >= n - 1:
            return 1
        jumps = 1
        steps = arr[0]
        for i in range(1, n):
            reach = max(reach, i + arr[i])
            if reach >= n - 1:
                return jumps + 1
            steps -= 1
            if steps == 0:
                if reach <= i:
                    return -1
                jumps += 1
                steps = reach - i
        return -1
