# User function Template for python3
# https://www.geeksforgeeks.org/problems/search-pattern-rabin-karp-algorithm--141631/1
class Solution:

    def get_hash(self, karp, start, end):
        if start == 0:
            return karp[end]
        return karp[end] - karp[start - 1]

    def search(self, pattern, text):
        # code here
        if len(pattern) > len(text):
            return []

        rabin_karp_pattern = [0 for _ in range(len(pattern))]
        rabin_karp_text = [0 for _ in range(len(text))]
        final_ans = []

        for i in range(len(pattern)):
            if i == 0:
                rabin_karp_pattern[0] = ord(pattern[0])
                continue
            rabin_karp_pattern[i] = ord(pattern[i]) + rabin_karp_pattern[i - 1]

        for i in range(len(text)):
            if i == 0:
                rabin_karp_text[0] = ord(text[0])
                continue
            rabin_karp_text[i] = ord(text[i]) + rabin_karp_text[i - 1]

        for i in range(len(text) - len(pattern) + 1):
            if self.get_hash(rabin_karp_pattern, 0, len(pattern) - 1) == self.get_hash(rabin_karp_text, i,
                                                                                       i + len(pattern) - 1):
                if text[i:i + len(pattern)] == pattern:
                    final_ans.append(i + 1)

        return final_ans