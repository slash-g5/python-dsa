# https://practice.geeksforgeeks.org/problems/generate-ip-addresses/1?page=4&sprint=a663236c31453b969852f9ea22507634&sprint=a663236c31453b969852f9ea22507634&sortBy=difficulty
class Solution:
    def genIp(self, s):
        # Code here
        ans = []
        n = len(s)
        for i in range(0, n-3):
            str1 = s[:i+1] + "."
            if str1[0] == '0' and len(str1) > 2:
                continue
            if int(s[:i+1]) > 255:
                continue
            for j in range(i+1, n-2):
                if s[i+1] == '0' and j != i+1:
                    continue
                if int(s[i+1: j+1]) > 255:
                    continue
                str2 = str1 + s[i+1: j+1] + "."
                for k in range(j+1, n-1):
                    if s[j+1] == '0' and k != j+1:
                        continue
                    if int(s[j+1: k+1]) > 255:
                        continue
                    if int(s[k+1: n]) > 255:
                        continue
                    if s[k+1] == '0' and k+1 != n-1:
                        continue
                    str3 = str2 + s[j+1:k+1] + "."
                    str3 += s[k+1:n]
                    ans.append(str3)
        if ans:
            return ans
        else:
            return [-1]