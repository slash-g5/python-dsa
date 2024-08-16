# https://leetcode.com/problems/maximum-segment-sum-after-removals/submissions/1358060152/

from sortedcontainers import SortedList
from typing import List
import heapq


class Solution:
    @staticmethod
    def maximumSegmentSum(nums: List[int], removeQueries: List[int]) -> List[int]:

        def findPoint(p, start, end):
            if start > end:
                return None
            if start == end:
                if sorted_list[start][0] <= p <= sorted_list[start][1]:
                    return sorted_list[start]
                return None
            mid = (start + end) // 2
            if sorted_list[mid][0] <= p <= sorted_list[mid][1]:
                return sorted_list[mid]
            if sorted_list[mid][0] > p:
                return findPoint(p, start, mid - 1)
            return findPoint(p, mid + 1, end)

        def getSum(tuple):
            return -(sumArr[tuple[1]] - sumArr[tuple[0] - 1] if tuple[0] > 0 else sumArr[tuple[1]])

        sumArr = []
        for num in nums:
            if not sumArr:
                sumArr = [num]
                continue
            sumArr.append(sumArr[-1] + num)

        sorted_list = SortedList()
        sorted_list.add((0, len(nums) - 1))
        ans = []
        heap = []
        to_remove = {}

        for i in range(len(removeQueries)):
            curr = findPoint(removeQueries[i], 0, len(sorted_list) - 1)
            sorted_list.discard(curr)
            val = sumArr[curr[1]] - sumArr[curr[0] - 1] if curr[0] > 0 else sumArr[curr[1]]
            if val in to_remove:
                to_remove[val] += 1
            else:
                to_remove[val] = 1
            if curr[0] == removeQueries[i]:
                if curr[1] > curr[0]:
                    sorted_list.add((curr[0] + 1, curr[1]))
                    heapq.heappush(heap, getSum((curr[0] + 1, curr[1])))
            elif curr[1] == removeQueries[i]:
                if curr[1] > curr[0]:
                    sorted_list.add((curr[0], curr[1] - 1))
                    heapq.heappush(heap, getSum((curr[0], curr[1] - 1)))
            else:
                sorted_list.add((curr[0], removeQueries[i] - 1))
                sorted_list.add((removeQueries[i] + 1, curr[1]))
                heapq.heappush(heap, getSum((curr[0], removeQueries[i] - 1)))
                heapq.heappush(heap, getSum((removeQueries[i] + 1, curr[1])))

            flag = True
            while heap:
                popped = -heapq.heappop(heap)
                if popped in to_remove:
                    if to_remove[popped] == 1:
                        del to_remove[popped]
                        continue
                    to_remove[popped] -= 1
                    continue
                ans.append(popped)
                flag = False
                heapq.heappush(heap, -popped)
                break

            if flag:
                ans.append(0)

        return ans
