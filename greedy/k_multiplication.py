# https://leetcode.com/problems/final-array-state-after-k-multiplication-operations-ii/
from typing import List
import heapq


class Solution:
    @staticmethod
    def getFinalState(nums: List[int], k: int, multiplier: int) -> List[int]:

        def maxI():
            ans = 0
            for i in range(len(nums)):
                if nums[i] > nums[ans]:
                    ans = i
            return ans

        def computePower(num, power):
            num %= (10 ** 9 + 7)
            if power == 0:
                return 1
            if power == 1:
                return num
            if power % 2 == 0:
                a = computePower(num, power // 2) % (10 ** 9 + 7)
                return (a * a) % (10 ** 9 + 7)
            a = computePower(num, (power - 1) // 2) % (10 ** 9 + 7)
            return (a * a * num) % (10 ** 9 + 7)

        if len(nums) == 1:
            nums[0] *= computePower(multiplier, k)
            nums[0] %= (10 ** 9 + 7)
            return nums

        if multiplier == 1:
            return nums

        heap = []
        maxi = maxI()

        for i in range(len(nums)):
            heapq.heappush(heap, (nums[i], i))

        k1 = 0
        while k1 < k:
            curr = heapq.heappop(heap)
            nums[curr[1]] *= multiplier
            k1 += 1
            heapq.heappush(heap, (nums[curr[1]], curr[1]))
            if curr[1] == maxi:
                break

        if k1 == k:
            for i in range(len(nums)):
                nums[i] %= (10 ** 9 + 7)
            return nums

        rem = k - k1

        rep = rem // len(nums)
        print(f'{multiplier=} {rep=}')

        multiRep = computePower(multiplier, rep)

        last = rem % len(nums)

        for i in range(len(nums)):
            nums[i] *= multiRep

        for i in range(last):
            curr = heapq.heappop(heap)
            nums[curr[1]] *= multiplier

        for i in range(len(nums)):
            nums[i] %= (10 ** 9 + 7)

        return nums


if __name__ == "__main__":
    s = Solution()
    print(s.getFinalState([66307295, 441787703, 589039035, 322281864], 900900704, 641725))
