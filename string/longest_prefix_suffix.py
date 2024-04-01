# https://www.geeksforgeeks.org/problems/longest-prefix-suffix2527/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=bottom_sticky_on_article
class Solution:
    def lps(self, s):
        # code here
        if len(s) < 2:
            return "0"
        lps = [0 for _ in range(len(s)+1)]
        lps[0] = -1
        i = 0
        j = -1
        while i < len(s):
            while j >= 0 and s[j] != s[i]:
                j = lps[j]
            lps[i+1] = j + 1
            i += 1
            j += 1
        return lps[len(s)]
