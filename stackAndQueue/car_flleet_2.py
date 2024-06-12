# https://leetcode.com/problems/car-fleet-ii/description/

from typing import List


class Solution:
    @staticmethod
    def getCollisionTimes(cars: List[List[int]]) -> List[float]:
        n = len(cars)
        times = [-1.0 for _ in range(n)]

        stack = [n - 1]

        for i in range(n - 1, -1, -1):
            while stack and (cars[stack[-1]][1] >= cars[i][1] or (
                    ((cars[stack[-1]][0] - cars[i][0]) / (cars[i][1] - cars[stack[-1]][1])) > times[stack[-1]] > 0)):
                stack.pop()
            if stack:
                relativeSpeed = cars[i][1] - cars[stack[-1]][1]
                dist = cars[stack[-1]][0] - cars[i][0]
                times[i] = dist / relativeSpeed

            stack.append(i)

        return times
