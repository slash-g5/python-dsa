# https://leetcode.com/problems/shortest-distance-after-road-addition-queries-ii/
from typing import List


class Solution:
    @staticmethod
    def shortestDistanceAfterQueries(n: int, queries: List[List[int]]) -> List[int]:
        relevant = {i for i in range(n)}
        second = [-1 for _ in range(n)]
        ans = []
        for i in range(len(queries)):
            if queries[i][0] in relevant and queries[i][1] in relevant:
                s = queries[i][0]
                queries[i][0] = second[queries[i][0]] - 1 if second[queries[i][0]] != -1 else queries[i][0]
                for j in range(queries[i][0] + 1, queries[i][1]):
                    relevant.discard(j)
                second[s] = queries[i][1]

            ans.append(len(relevant) - 1)
        return ans
