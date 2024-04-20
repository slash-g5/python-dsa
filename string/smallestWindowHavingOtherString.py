# User function Template for python3
# https://www.geeksforgeeks.org/problems/smallest-window-in-a-string-containing-all-the-characters-of-another-string-1587115621/1
import sys


class Solution:

    # Function to find the smallest window in the string s consisting
    # of all the characters of string p.
    @staticmethod
    def smallestWindow(s, p):
        # code here
        ans = (-1, -1)
        min_len = sys.maxsize

        map_P = {}
        set_P = set()

        for c in p:
            set_P.add(c)
            if c not in map_P:
                map_P[c] = 1
            else:
                map_P[c] += 1

        start = 0
        end = 0

        while end < len(s):
            if s[end] not in map_P:
                if start == end:
                    start += 1
                end += 1
                continue
            map_P[s[end]] -= 1
            if map_P[s[end]] == 0:
                set_P.remove(s[end])
                if not set_P:
                    for i in range(start, end + 1):
                        if s[i] not in map_P:
                            continue
                        map_P[s[i]] += 1
                        if map_P[s[i]] == 1:
                            start = i
                            if min_len > end - start + 1:
                                min_len = end - start + 1
                                ans = (start, end)
                            start += 1
                            set_P.add(s[i])
                            break
            end += 1

        return "-1" if ans == (-1, -1) else ''.join(s[ans[0]: ans[1] + 1])
