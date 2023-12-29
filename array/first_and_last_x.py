# User function Template for python3
# https://practice.geeksforgeeks.org/problems/first-and-last-occurrences-of-x3116/1

def find_helper(arr, left, right, x):
    if arr[right] < x or arr[left] > x:
        return -1, -1
    if right < left:
        return -1, -1
    if right == left:
        if arr[right] == x:
            return right, right
        return -1, -1
    mid = (left + right) // 2
    f1, f2 = find_helper(arr, left, mid, x)
    l1, l2 = find_helper(arr, mid + 1, right, x)
    if f1 != -1 and l2 != -1:
        return f1, l2
    if f1 == -1 and l2 == -1:
        return -1, -1
    if f1 == -1:
        return l1, l2
    if l1 == -1:
        return f1, f2


class Solution:

    def find(self, arr, n, x):
        ans = []
        f1, f2 = find_helper(arr, 0, n - 1, x)
        ans.append(f1)
        ans.append(f2)
        return ans
