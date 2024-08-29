# https://leetcode.com/problems/count-substrings-that-satisfy-k-constraint-ii/
from typing import List


class Solution:
    @staticmethod
    def countKConstraintSubstrings(s: str, k: int, queries: List[List[int]]) -> List[int]:

        def getIndex(l, r, end):
            if l == r:
                return r
            if l == r - 1:
                if l + most_value[l] - 1 >= end:
                    return l
                return r
            mid = (l + r) // 2
            if most_value[mid] + mid - 1 >= end:
                return getIndex(l, mid, end)
            else:
                return getIndex(mid + 1, r, end)

        def countSubStr(l, r):
            index = getIndex(l, r, r)
            c1 = num_substr[l] - num_substr[index]
            c1 = max(c1, 0)
            c2 = ((r - index + 1) * (r - index + 2)) // 2
            return c1 + c2

        most_value = [i for i in range(len(s))]
        n = len(s)
        currIndex = 0
        end = 0
        z_cnt = 0
        o_cnt = 0

        while currIndex < n:

            if end < currIndex:
                end = currIndex
                z_cnt = 0
                o_cnt = 0

            if end >= n:
                most_value[currIndex] = n - currIndex
                currIndex += 1
                continue

            if s[end] == '0':
                z_cnt += 1
            else:
                o_cnt += 1

            if z_cnt <= k or o_cnt <= k:
                end += 1
                continue

            most_value[currIndex] = end - currIndex

            if end >= n:
                continue

            next = currIndex + 1
            while next <= end:
                if s[next - 1] == '0':
                    z_cnt -= 1
                else:
                    o_cnt -= 1
                if z_cnt > k and o_cnt > k:
                    most_value[next] = end - next
                    next += 1
                    continue
                else:
                    break

            currIndex = next
            end += 1

        num_substr = most_value.copy()

        for i in range(n - 2, -1, -1):
            num_substr[i] = num_substr[i] + num_substr[i + 1]

        q = len(queries)
        ans = []

        for i in range(q):
            l = queries[i][0]
            r = queries[i][1]
            temp = countSubStr(l, r)
            ans.append(temp)

        return ans
