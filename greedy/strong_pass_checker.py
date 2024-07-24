# https://leetcode.com/problems/strong-password-checker/submissions/1332252821/
class Solution:
    @staticmethod
    def strongPasswordChecker(password: str) -> int:

        def findRCount(start):
            if start == len(password) - 1:
                return 1
            ans = 1
            for i in range(start + 1, len(password)):
                if password[i] == password[start]:
                    ans += 1
                else:
                    return ans
            return ans

        def numAtLeast(lower, upper, digit):
            if not (lower or digit or upper):
                return 3
            elif lower and digit and upper:
                return 0
            elif lower ^ digit ^ upper:
                return 2
            else:
                return 1

        def less20Ans(ans, lower, upper, digit):
            if ans > 1:
                return ans
            if ans == 1 and numAtLeast(lower, upper, digit) <= 1:
                return 1
            if ans == 1:
                return 2
            if numAtLeast(lower, upper, digit) > 0:
                return numAtLeast(lower, upper, digit)
            if len(password) == 5:
                return 1
            return 0

        def findRnD():
            zCount, oCount, tCount = [], [], []
            currCount = 0
            maxCount = max(len(password) - 20, 0)
            i = 0
            lower, upper, digit = False, False, False

            while i < len(password):
                if not lower and ord('a') <= ord(password[i]) <= ord('z'):
                    lower = True
                if not upper and ord('A') <= ord(password[i]) <= ord('Z'):
                    upper = True
                if not digit and ord('0') <= ord(password[i]) <= ord('9'):
                    digit = True
                rCount = findRCount(i)
                print(f'i = {i} rCount = {rCount}')
                i += rCount
                if rCount < 3:
                    continue
                if rCount % 3 == 0:
                    zCount.append(rCount // 3)
                if rCount % 3 == 1:
                    oCount.append(rCount // 3)
                if rCount % 3 == 2:
                    tCount.append(rCount // 3)

            while currCount < maxCount and (zCount or oCount or tCount):

                if currCount > maxCount - 1:
                    break
                if currCount > maxCount - 2 and (not zCount):
                    break
                if currCount > maxCount - 3 and (not zCount and not oCount):
                    break

                while zCount:
                    if currCount > maxCount - 1:
                        break
                    curr = zCount.pop()
                    if curr > 1:
                        tCount.append(curr - 1)
                    currCount += 1

                while oCount:
                    if currCount > maxCount - 2:
                        break
                    curr = oCount.pop()
                    if curr > 1:
                        tCount.append(curr - 1)
                    currCount += 2

                while tCount:
                    if currCount > maxCount - 3:
                        break
                    curr = tCount.pop()
                    if curr > 1:
                        tCount.append(curr - 1)
                    currCount += 3

            rCount = sum(zCount) + sum(oCount) + sum(tCount)

            return maxCount + less20Ans(rCount, lower, upper, digit)

        print(len(password))
        if len(password) < 5:
            return 6 - len(password)
        return findRnD()
