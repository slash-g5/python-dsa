# https://leetcode.com/problems/regular-expression-matching/
class Solution:

    def helper(self, s, p, startS, startP, memo):
        if (startS, startP) in memo:
            return memo[(startS, startP)]
        if startS < len(s) and startP == len(p):
            memo[(startS, startP)] = False
            return False
        if startS == len(s) and startP == len(p):
            memo[(startS, startP)] = True
            return True
        if startS == len(s) and startP < len(p):
            for i in range(startP, len(p)):
                if p[i] != '*':
                    if i + 1 < len(p) and p[i + 1] == '*':
                        continue
                    memo[(startS, startP)] = False
                    return False
            memo[(startS, startP)] = True
            return True

        if s[startS] == p[startP] or p[startP] == '.':
            if startP == len(p) - 1 or p[startP + 1] != '*':
                memo[(startS, startP)] = self.helper(s, p, startS + 1, startP + 1, memo)
                return memo[(startS, startP)]
            memo[(startS, startP)] = (self.helper(s, p, startS + 1, startP + 2, memo)
                                      or self.helper(s, p, startS, startP + 2, memo)
                                      or self.helper(s, p, startS + 1, startP, memo))
            return memo[(startS, startP)]

        if startP < len(p) - 1 and p[startP + 1] == '*':
            memo[(startS, startP)] = self.helper(s, p, startS, startP + 2, memo)
            return memo[(startS, startP)]

        memo[(startS, startP)] = False
        return False

    def isMatch(self, s: str, p: str) -> bool:
        if s == '' and (p == '' or p == '*'):
            return True
        return self.helper(s, p, 0, 0, {})
