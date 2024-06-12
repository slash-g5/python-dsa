# https://leetcode.com/problems/car-fleet/

from typing import List


class Solution:
    @staticmethod
    def carFleet(target: int, position: List[int], speed: List[int]) -> int:

        def getTime(target, position, speed):
            return (target - position) / speed

        n = len(position)
        pos_speed = list(zip(position, speed))
        pos_speed.sort(key=lambda x: x[0])

        ans = 1
        stack = [n - 1]

        for i in range(n - 2, -1, -1):
            while stack and getTime(target, pos_speed[stack[-1]][0], pos_speed[stack[-1]][1]) < getTime(target,
                                                                                                        pos_speed[i][0],
                                                                                                        pos_speed[i][
                                                                                                            1]):
                stack.pop()
            if not stack:
                ans += 1
            stack.append(i)

        return ans
