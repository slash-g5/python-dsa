# https://leetcode.com/problems/count-collisions-on-a-road/
class Solution:
    @staticmethod
    def countCollisions(directions: str) -> int:
        # RLRSLL
        stack = []
        n = len(directions)
        # [L] 0
        # [LL] 0
        # [S L] 2
        # [S L] 3
        # [S L] 4
        # [L S L] 4
        # [S S L] 6
        # [S S] 7

        # [R] 0
        # [S] 2
        # [S R] 2
        # [S R R] 2
        # [S R R R] 2
        # [S S] 6
        # [S S] 7

        # RRLSLL
        # [R] 0
        # [RR] 0
        # [S] 3
        # [SS] 3
        # [SS] 4
        # [SS] 5
        ans = 0

        for i in range(n):
            if not stack:
                stack.append(directions[i])
                continue
            # S => check for all R's in stack
            # L => Check for all R's in stack, if S is found then merge
            # R => stack.append
            if directions[i] == 'R':
                stack.append('R')
                continue
            if directions[i] == 'L':
                curr = 0
                while stack and stack[-1] == 'R':
                    curr += 1
                    stack.pop()
                if curr != 0:
                    ans += curr + 1
                    stack.append('S')
                    continue
                while stack and stack[-1] == 'S':
                    curr += 1
                    stack.pop()
                    break
                if curr == 0:
                    stack.append('L')
                    continue
                stack.append('S')
                ans += curr
                continue
            if directions[i] == 'S':
                curr = 0
                while stack and stack[-1] == 'R':
                    curr += 1
                    stack.pop()
                stack.append('S')
                ans += curr

        return ans
