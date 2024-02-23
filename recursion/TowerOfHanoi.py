# User function Template for python3

class Solution:

    def print_step(self, diskNo, source1, destination):
        print('move disk ' + str(diskNo) + ' from rod ' + source1 + ' to rod ' + destination)

    def toh_helper(self, fromm, to, aux, N):
        if N == 0:
            return 0
        if N == 1:
            self.print_step(N, fromm, to)
            return 1
        temp = self.toh_helper(fromm, aux, to, N - 1)
        self.print_step(N, fromm, to)
        temp1 = self.toh_helper(aux, to, fromm, N - 1)
        return temp + temp1 + 1

    def toh(self, N, fromm, to, aux):
        # Your code here
        return self.toh_helper(str(fromm), str(to), str(aux), N)


# {
# Driver Code Starts
# Initial Template for Python 3


import math


def main():
    ob = Solution()
    print(ob.toh(1, 1, 3, 2))


if __name__ == "__main__":
    main()

# } Driver Code Ends