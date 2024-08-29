# https://leetcode.com/problems/find-the-largest-palindrome-divisible-by-k/
class Solution:

    @staticmethod
    def subtractStr(large, small, begin, end):
        s = len(small) - 1
        l = end
        while l >= begin:
            if s < 0:
                return large
            if s >= 0 and large[l] >= small[s]:
                large[l] = str(int(large[l]) - int(small[s]))
                l -= 1
                s -= 1
                continue
            if s >= 0 and large[l] < small[s]:
                curr = l - 1
                while large[curr] == '0':
                    large[curr] = '9'
                    curr -= 1
                large[curr] = str(int(large[curr]) - 1)
                large[l] = str(10 + int(large[l]) - int(small[s]))
                l -= 1
                s -= 1

    def checkDivisibleBy7(self, num, begin, end):
        if num == '7' or num == '0':
            return True
        if begin > end:
            return True
        if begin == end:
            return False

        if end - begin + 1 < 5:
            intV = int(''.join(num[begin:end + 1]))
            if intV % 7 == 0:
                return True
            return False

        h2 = str(2 * int(num[end]))
        return self.checkDivisibleBy7(self.subtractStr(num, h2, begin, end - 1), begin, end - 1)

    def largestPalindrome(self, n: int, k: int) -> str:
        if k == 1 or k == 3 or k == 9:
            ans = []
            for i in range(n):
                ans.append('9')
            return ''.join(ans)
        if k == 5:
            ans = []
            if n == 1:
                return '5'
            if n == 2:
                return '55'
            ans.append('5')
            for i in range(n - 2):
                ans.append('9')
            ans.append('5')
            return ''.join(ans)
        if k == 2:
            if n == 1:
                return '8'
            if n == 2:
                return '88'
            ans = ['8']
            for i in range(n - 2):
                ans.append('9')
            ans.append('8')
            return ''.join(ans)
        if k == 4:
            if n == 1:
                return '8'
            if n == 2:
                return '88'
            if n == 3:
                return '888'
            if n == 4:
                return '8888'
            ans = ['88']
            for _ in range(n - 4):
                ans.append('9')
            ans.append('88')
            return ''.join(ans)
        if k == 8:
            if n == 1:
                return '8'
            if n == 2:
                return '88'
            if n == 3:
                return '888'
            if n == 4:
                return '8888'
            if n == 5:
                return '88888'
            if n == 6:
                return '888888'
            ans = ['888']
            for i in range(n - 6):
                ans.append('9')
            ans.append('888')
            return ''.join(ans)
        if k == 6:
            if n == 1:
                return '6'
            if n == 2:
                return '66'
            if n == 3:
                return '888'
            if n == 4:
                return '8778'
            if n % 2 == 1:
                mid = n // 2
                ans = ['8']
                for i in range(n - 2):
                    if i == mid - 1:
                        ans.append('8')
                    else:
                        ans.append('9')
                ans.append('8')
                return ''.join(ans)
            else:
                mid1 = n // 2
                mid2 = n // 2 - 1
                ans = ['8']
                for i in range(n - 2):
                    if mid1 == i + 1 or mid2 == i + 1:
                        ans.append('7')
                    else:
                        ans.append('9')
                ans.append('8')
                return ''.join(ans)
        if k == 7:
            if n == 1:
                return '7'
            if n == 2:
                return '77'
            ans = []
            if n % 2 == 1:
                mid = n // 2
                for i in range(n):
                    ans.append('9')
                for i in range(9, -1, -1):
                    ans[mid] = str(i)
                    if self.checkDivisibleBy7(ans.copy(), 0, n - 1):
                        return ''.join(ans)
            if n % 2 == 0:
                mid1 = n // 2
                mid2 = n // 2 - 1
                for i in range(n):
                    ans.append('9')
                for i in range(9, -1, -1):
                    ans[mid1] = str(i)
                    ans[mid2] = str(i)
                    if self.checkDivisibleBy7(ans.copy(), 0, n - 1):
                        return ''.join(ans)
            ans = []
            for _ in range(n):
                ans.append('7')
            return ''.join(ans)
