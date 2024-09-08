# https://leetcode.com/problems/majority-element-ii/
from typing import List


class Solution:

    @staticmethod
    def majorityElement(nums: List[int]) -> List[int]:
        def checkMajority():
            c1 = 0
            c2 = 0
            for num in nums:
                if m1 == num:
                    c1 += 1
                if m2 == num:
                    c2 += 1
            ans = []
            if c1 > len(nums) // 3:
                ans.append(m1)
            if c2 > len(nums) // 3:
                ans.append(m2)
            return ans

        m1 = 0
        m2 = 1
        n1 = 0
        n2 = 0

        for num in nums:
            if m1 == num:
                n1 += 1
                continue
            if m2 == num:
                n2 += 1
                continue
            if n1 == 0:
                m1 = num
                n1 = 1
                continue
            if n2 == 0:
                m2 = num
                n2 = 1
                continue
            n1 -= 1
            n2 -= 1

        return checkMajority()
