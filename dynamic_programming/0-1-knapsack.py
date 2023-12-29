class Solution:
    # Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self, W, wt, val, n):
        tab = [[-1 for _ in range(W + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            tab[i][0] = 0
        for j in range(W + 1):
            tab[0][j] = 0
        for i in range(1, n + 1):
            for j in range(1, W + 1):
                if j >= wt[i - 1]:
                    tab[i][j] = max(tab[i - 1][j], val[i - 1] + tab[i - 1][j - wt[i - 1]])
                else:
                    tab[i][j] = tab[i - 1][j]
        return tab[n][W]
