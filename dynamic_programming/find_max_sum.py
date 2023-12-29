class Solution:

    # Function to find the maximum money the thief can get.
    def FindMaxSum(self, a, n):
        dp_array = [None for _ in range(n)]
        if n == 1:
            return a[n - 1]
        if n == 2:
            return max(a[0], a[1])
        dp_array[n - 1] = a[n - 1]
        dp_array[n - 2] = max(a[n - 2], a[n - 1])
        for i in range(n - 3, -1, -1):
            dp_array[i] = max(a[i] + dp_array[i + 2], dp_array[i + 1])
        return dp_array[0]
