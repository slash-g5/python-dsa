# User function Template for python3
# https://www.geeksforgeeks.org/problems/finding-the-numbers0215/1?page=1&category=Bit%20Magic&sortBy=submissions
class Solution:
    def singleNumber(self, nums):

        def all_xor(input_arr):
            ans = 0
            for a in input_arr:
                ans ^= a
            return ans

        def get_first_set_bit(num, curr=0):
            if num == 0:
                return -1
            if num % 2 == 0:
                return get_first_set_bit(num // 2, curr + 1)
            if num % 2 == 1:
                return curr + 1

        def check_ith_bit_set(num, i, curr=1):
            if curr == i:
                if num % 2 == 0:
                    return True
                else:
                    return False
            return check_ith_bit_set(num // 2, i, curr + 1)

        all_xor = all_xor(nums)
        first_set = get_first_set_bit(all_xor)
        mask = all_xor & (-all_xor)

        ans = [0, 0]

        for num in nums:
            if check_ith_bit_set(num, first_set):
                ans[1] ^= num
            else:
                ans[0] ^= num

        return min(ans), max(ans)


# {
# Driver Code Starts
# Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        v = list(map(int, input().split()))
        ob = Solution();
        ans = ob.singleNumber(v)
        for i in ans:
            print(i, end=" ")
        print()

# } Driver Code Ends