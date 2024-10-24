# https://leetcode.com/problems/check-if-dfs-strings-are-palindromes/
class Solution:

    def getLPSArray(self, s: str):

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
                left_boundary = centre - lps[centre] // 2
                mir_curr = 2 * centre - curr
                mir_boundary = mir_curr - lps[mir_curr] // 2
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
        return lps

    def findAnswer(self, parent: List[int], s: str) -> List[bool]:
        def getAdj():
            adj = [[] for _ in range(len(s))]
            for i in range(len(parent)):
                if parent[i] == -1:
                    continue
                adj[parent[i]].append(i)
            return adj

        def dfs(start):
            if not adj[start]:
                rDfs.append(start)
                nodeCount[start] = 1
                return
            for node in adj[start]:
                dfs(node)
                nodeCount[start] += nodeCount[node]
            rDfs.append(start)
            nodeCount[start] += 1

        def lpsIndx(charIndex):
            return 2 * charIndex + 1

        adj = getAdj()
        rDfs = []
        nodeCount = [0 for _ in range(len(s))]
        dfs(0)
        lps = self.getLPSArray(''.join([s[i] for i in rDfs]))
        boolDfs = [False for _ in range(len(s))]

        #   #a#b#a#a#b#a#

        for i in range(len(rDfs)):
            if nodeCount[rDfs[i]] <= 1:
                boolDfs[rDfs[i]] = True
                continue
            end = lpsIndx(i)
            start = end - 2 * (nodeCount[rDfs[i]] - 1)
            if ((end + start) // 2 + lps[(end + start) // 2] // 2) >= end:
                boolDfs[rDfs[i]] = True

        return boolDfs
