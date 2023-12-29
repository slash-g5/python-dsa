class Solution:
    # Function to find triplets with zero-sum.
    def findTriplets(self, arr, n):
        arr.sort()
        for i in range(n-2):
            ignore_index = i
            required_sum = -arr[i]
            start = i + 1
            end = n-1
            while start < end and start < n and end > 0:
                if start == ignore_index:
                    start += 1
                    continue
                if end == ignore_index:
                    end -= 1
                    continue
                temp_sum = arr[start] + arr[end]
                if temp_sum == required_sum:
                    return True
                if temp_sum < required_sum:
                    start += 1
                    continue
                if temp_sum > required_sum:
                    end -= 1
                    continue
        return False
