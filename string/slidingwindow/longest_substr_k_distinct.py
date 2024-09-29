# https://www.geeksforgeeks.org/problems/longest-k-unique-characters-substring0853/1
class Solution:

    @staticmethod
    def longestKSubstr(s, k):
        # code here

        if k == 0:
            return 0

        t_dict = {}
        left = 0
        right = 0
        ans = -1

        while left < len(s) and right < len(s):

            if s[right] in t_dict:
                t_dict[s[right]] += 1
            else:
                t_dict[s[right]] = 1

            if len(t_dict) == k:
                ans = max(ans, right - left + 1)
                right += 1
                continue

            if len(t_dict) < k:
                right += 1
                continue

            right += 1

            while len(t_dict) > k and left < right:
                t_dict[s[left]] -= 1
                if t_dict[s[left]] == 0:
                    del t_dict[s[left]]
                left += 1

        return ans
