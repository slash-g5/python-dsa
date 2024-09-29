# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/?envType=problem-list-v2&envId=sliding-window&difficulty=MEDIUM
class Solution:
    @staticmethod
    def numberOfSubstrings(s: str) -> int:

        def containsAll():
            return ('a' in t_dict and 'b' in t_dict and 'c' in t_dict
                    and t_dict['a'] > 0 and t_dict['b'] > 0 and t_dict['c'] > 0)

        left = 0
        right = 0
        t_dict = {}
        ans = 0

        while left < len(s) and right < len(s):
            if s[right] in t_dict:
                t_dict[s[right]] += 1
            else:
                t_dict[s[right]] = 1
            if not containsAll():
                right += 1
                continue
            # right, right+1, ..., len(s)-1
            while containsAll():
                ans += len(s) - right
                t_dict[s[left]] -= 1
                left += 1
            right += 1

        return ans



