class Solution:
    class Solution:

        def findSubarray(self, a, n):
            # code here
            # [1,2,3, -1, 2] => [all]
            if not a:
                return [-1]
            max_until_now = curr_max = 1, 0, a[0]  # size, start_index, sum

            for i in range(1, n):
                if max_until_now[2] <= 0:
                    if a[i] > max_until_now[2]:
                        max_until_now = curr_max = 1, i, a[i]  # array, size, start_index
                    else:
                        curr_max = 1, i, a[i]
                    continue
                if a[i] >= 0 and curr_max[2] >= 0:
                    curr_max = curr_max[0] + 1, curr_max[1], curr_max[2] + a[i]
                    if curr_max[2] > max_until_now[2]:
                        max_until_now = curr_max
                    if curr_max[2] == max_until_now[2] and curr_max[0] > max_until_now[0]:
                        max_until_now = curr_max
                    continue
                if a[i] >= 0 and curr_max[2] < 0:
                    curr_max = 1, i, a[i]
                    if curr_max[2] > max_until_now[2]:
                        max_until_now = curr_max
                    if curr_max[2] == max_until_now[2] and curr_max[0] > max_until_now[0]:
                        max_until_now = curr_max
                    continue
                if a[i] < 0:
                    curr_max = 1, i, a[i]
            return a[max_until_now[1]: max_until_now[1] + max_until_now[0]]
