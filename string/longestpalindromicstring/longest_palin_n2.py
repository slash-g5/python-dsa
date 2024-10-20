# https://leetcode.com/problems/longest-palindromic-substring/
# n**2 solution
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        mid = 0
        ans = 1
        start = 0
        while mid < len(s):
            # check odd
            cnt = 1
            l = mid - 1
            r = mid + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                cnt += 2
            if cnt > ans:
                ans = cnt
                start = l + 1
            # check even
            cnt = 0
            l = mid
            r = mid + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
                cnt += 2
            if cnt > ans:
                ans = cnt
                start = l + 1
            mid += 1
        return s[start:start + ans]
