# https://www.geeksforgeeks.org/problems/form-a-palindrome1455/1
class Solution:
    def countMin(self, Str):
        # code here
        tab = [[0 for _ in range(len(Str))] for _ in range(len(Str))]
        for diff in range(1, len(Str)):
            for i in range(len(Str)):
                if i + diff >= len(Str):
                    break
                if Str[i] == Str[i+diff]:
                    tab[i][i+diff] = tab[i+1][i+diff-1]
                else:
                    tab[i][i+diff] = 1 + min(tab[i+1][i+diff], tab[i][i-1+diff])
        return tab[0][len(Str) - 1]