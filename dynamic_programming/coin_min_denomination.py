# https://www.geeksforgeeks.org/problems/-minimum-number-of-coins4426/1
import sys
class Solution:

    def minPartitionHelper(self, N, mem={}):
        if N == 0:
            return 0, []
        if N in mem:
            return mem[N]
        currency = [1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]
        ans = (N, [1 for _ in range(N)])
        for curr in currency:
            if N - curr < 0:
                continue
            curr_ans = self.minPartitionHelper(N - curr, mem)
            if ans[0] > curr_ans[0] + 1:
                ans = curr_ans[0] + 1, curr_ans[1] +  [curr]
        mem[N] = ans
        return ans


if __name__ == "__main__":
    sys.setrecursionlimit(50000)
    solution = Solution()
    print(solution.minPartitionHelper(8098))
