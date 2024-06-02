# User function Template for python3
from collections import deque

import sys


class Solution:

    def rremove_helper(self, S, curr):
        last_removed = '~'
        if curr > len(S) - 1:
            return ('', last_removed)
        if curr == len(S) - 1:
            return (S[-1], last_removed)
        ans = ''
        if S[curr] != S[curr + 1]:
            temp = self.rremove_helper(S, curr + 1)
            ans += temp[0]
            ans = S[curr] + ans
            cut_index = 0
            # print('ans= ', ' ')
            # print(ans)
            if S[curr] == temp[1]:
                return ans[1:], temp[1]

            while cut_index < len(ans) - 1 and ans[0] == ans[cut_index + 1]:
                last_removed = ans[cut_index + 1]
                cut_index += 1

            # print('_'*25)
            # print('last removed = ' + last_removed)
            # print(ans)
            # print(cut_index)
            return (ans, last_removed) if cut_index == 0 else (ans[cut_index + 1:], last_removed)

        if S[curr] == S[curr + 1]:
            i = curr
            while i < len(S) - 1 and S[i] == S[i + 1]:
                i += 1
            temp = self.rremove_helper(S, i + 1)
            return (temp[0], temp[1])

    def rremove(self, S):
        # code here
        sys.setrecursionlimit(18000)
        return self.rremove_helper(S, 0)[0]


if __name__ == "__main__":
    test = Solution()
    test.rremove("abbcbbcaa")