# https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii/description/
class Solution:
    @staticmethod
    def countOfSubstrings(word: str, k: int) -> int:

        def isVowel(char):
            return char == 'e' or char == 'a' or char == 'i' or char == 'o' or char == 'u'

        def allVowels(l, r):
            if l > r - 4:
                return False
            v_dict = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
            for k in v_dict:
                v_dict[k] = v_map[right][k] - v_map[left - 1][k] if left > 0 else v_map[right][k]
            return (v_dict['a'] > 0 and v_dict['e'] > 0 and v_dict['i'] > 0 and v_dict['o'] > 0
                    and v_dict['u'] > 0)

        def getNextConsonant(index, start, end):
            if start > end:
                return -1
            if consonants[end] < index:
                return -1
            if start == end:
                return consonants[start]
            if end == start + 1:
                if consonants[start] >= index:
                    return consonants[start]
                return consonants[end]
            mid = (start + end) // 2
            if consonants[mid] < index:
                return getNextConsonant(index, mid + 1, end)
            if consonants[mid] >= index:
                if consonants[mid - 1] < index:
                    return consonants[mid]
                return getNextConsonant(index, start, mid - 1)

        def getNextConsonantEx(index, start, end):
            if not isVowel(word[index]):
                return getNextConsonant(index + 1, start, end)
            else:
                return getNextConsonant(index, start, end)

        def vowelSum():
            v_dict = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
            v_map = []
            for i in range(len(word)):
                if word[i] in v_dict:
                    v_dict[word[i]] += 1
                v_map.append(v_dict.copy())
            return v_map

        consonants = []
        for i in range(len(word)):
            if not isVowel(word[i]):
                consonants.append(i)
        num_c = len(consonants)

        left = 0
        right = 0

        v_map = vowelSum()

        # print(f'{v_map=}')

        c_count = 0

        ans = 0

        while left < len(word):

            # print(f'{left=} {right=}')

            if not isVowel(word[right]):
                c_count += 1

            if c_count < k:
                if right == len(word) - 1:
                    # print('oops')
                    return ans
                right += 1
                continue

            if c_count == k + 1:
                nc = getNextConsonant(left, 0, num_c - 1)
                if nc == -1:
                    return ans
                left = nc + 1
                c_count = k

            while allVowels(left, right):
                # print('here')
                nc = getNextConsonantEx(right, 0, num_c - 1)
                if nc == -1:
                    ans += len(word) - right
                else:
                    ans += nc - right
                left += 1
                if not isVowel(word[left - 1]):
                    c_count -= 1
                    break

            if right == len(word) - 1:
                return ans
            right += 1

        return ans
