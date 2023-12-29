# https://practice.geeksforgeeks.org/problems/longest-palindrome-in-a-string3411/1
class Solution:
    def longestPalin(self, S):
        # code here
        if not S:
            return ""
        ans = S[0]
        for i in range(0, len(S)):
            # check odd palindrome length
            odd = 1
            left = i - 1
            right = i + 1
            while left >= 0 and right < len(S):
                if S[left] == S[right]:
                    odd += 2
                else:
                    break
                left -= 1
                right += 1

            # check even palindrome length
            even = 0
            left = i
            right = i + 1
            while left >= 0 and right < len(S):
                if S[left] == S[right]:
                    even += 2
                else:
                    break
                left -= 1
                right += 1

            if odd > max(len(ans), even):
                ans = S[(i - odd // 2):(i + odd // 2 + 1)]
            if even > max(len(ans), odd):
                ans = S[(i - even // 2 + 1):(i + even // 2 + 1)]

        return ans
