# https://practice.geeksforgeeks.org/problems/coin-change2448/1?page=2&sprint=a663236c31453b969852f9ea22507634&sprint=a663236c31453b969852f9ea22507634&sortBy=submissions

class Solution:

    def count(self, coins, N, Sum):
        # code here
        coins.sort()

        dp_array = [0 for _ in range(Sum + 1)]
        dp_array[0] = 1

        for coin in coins:
            for i in range(coin, Sum + 1):
                dp_array[i] += dp_array[i - coin]
        return dp_array[Sum]

