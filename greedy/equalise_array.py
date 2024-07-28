# https://leetcode.com/problems/minimum-cost-to-equalize-array/

import sys
from typing import List

class Solution:

    def equaliseToValue(self, nums, cost1, cost2, value, sumG, maxG):
        # gaps = [(value - nums[i]) for i in range(len(nums))]
        # maxG = max(gaps)
        # sumG = sum(gaps)
        if 2 * maxG == sumG:
            return (cost2 * maxG), True
        elif 2 * maxG > sumG:
            pairable = (sumG - maxG)
            return (pairable * cost2) + ((2 * maxG - sumG) * cost1), False
        elif 2 * maxG < sumG and sumG % 2 == 1:
            return (cost2 * (sumG // 2)) + cost1, False
        else:
            return cost2 * (sumG // 2), True

    def minCostToEqualizeArray(self, nums: List[int], cost1: int, cost2: int) -> int:
        if len(nums) <= 1:
            return 0
        if len(nums) == 2:
            return (cost1 * (max(nums) - min(nums))) % (10 ** 9 + 7)

        if cost2 >= 2 * cost1:
            mNum = max(nums)
            ans = 0
            for num in nums:
                ans += ((mNum - num) * cost1)
            return ans % (10 ** 9 + 7)

        mNum = max(nums)

        sumG = 0
        maxG = 0
        for i in range(len(nums)):
            sumG += mNum - nums[i]
            maxG = max(maxG, mNum - nums[i])

        ans = sys.maxsize
        i = mNum
        while True:
            if i > mNum:
                sumG += len(nums)
                maxG += 1
            if (sumG * cost2) // 2 > ans:
                break
            t_ans = self.equaliseToValue(nums, cost1, cost2, i, sumG, maxG)
            ans = min(ans, t_ans[0])
            if t_ans[1]:
                break
            i += 1

        return ans % (10 ** 9 + 7)