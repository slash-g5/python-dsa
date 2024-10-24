# https://leetcode.com/problems/longest-palindromic-substring/
# O(n) solution, manachers algorithm

class Solution:
    def longestPalindrome(self, s: str) -> str:
        def getChar(i):
            if i % 2 == 0:
                return '#'
            return s[i // 2]

        if len(s) <= 1:
            return s
        n = len(s)
        lps = [1 for _ in range(2 * n + 1)]
        curr = 1
        centre = 0
        r = 0

        while curr < 2 * n + 1:
            # case 1 curr >= r
            if curr >= r:
                c_cnt = 1
                c_r = curr + 1
                c_l = curr - 1
                while c_r < 2 * n + 1 and c_l >= 0 and getChar(c_r) == getChar(c_l):
                    c_cnt += 2
                    c_r += 1
                    c_l -= 1
                lps[curr] = c_cnt
                r = c_r - 1
                centre = curr
                curr += 1
                continue
            else:
                # case 2 curr < r
                # centre - mir_curr = curr - centre
                # centre - l = r - centre
                left_boundary = centre - lps[centre]//2
                mir_curr = 2 * centre - curr
                mir_boundary = mir_curr - lps[mir_curr]//2
                mir_lps = lps[mir_curr]
                if mir_boundary > left_boundary:
                    lps[curr] = mir_lps
                    curr += 1
                    continue
                else:
                    c_r = r + 1
                    # c_r - curr = curr - c_l
                    c_l = 2 * curr - c_r
                    c_cnt = 2 * (r - curr) + 1
                    while c_r < 2 * n + 1 and c_l >= 0 and getChar(c_r) == getChar(c_l):
                        c_l -= 1
                        c_r += 1
                        c_cnt += 2
                    lps[curr] = c_cnt
                    if c_r > r + 1:
                        r = c_r - 1
                        centre = curr
                    curr += 1
                    continue
        max_len = 0
        centre = 0
        for i in range(2 * n + 1):
            t_len = i % 2
            num_doubles = (lps[i] - i % 2) // 2
            if i % 2 == 1:
                t_len += (num_doubles//2)*2
            else:
                t_len += ((num_doubles+1)//2)*2
            if t_len > max_len:
                max_len = t_len
                centre = i
        print(f'{max_len=} {centre=}')
        l = centre - 1
        r = centre + 1
        while l >= 0 and r < 2*n + 1 and getChar(l) == getChar(r):
            l -= 1
            r += 1
        print(f'{l=} {r=} {lps=}')
        for i in range(2*n+1):
            print(f'{i=} {getChar(i)}')
        ans = []
        for i in range(l+1, r):
            if getChar(i) != '#':
                ans.append(getChar(i))
        return ''.join(ans)


if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("bacabab"))
