class Solution:
    # Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W, arr, n):
        arr.sort(key=lambda x: x.weight/x.value)
        ans = 0
        for a in arr:
            if a.weight > W:
                ans += (W/a.weight)*a.value
                return ans
            else:
                ans += a.value
                W -= a.weight
        return ans
