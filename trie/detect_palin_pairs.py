import trie_search_insert


def buildPalinEndMap(word, palinEndMAp):
    if word not in palinEndMAp:
        palinEndMAp[word] = 0
    curr_word = ''
    for i in range(len(word) - 1):
        curr_word += word[i]
        if curr_word in palinEndMAp and palinEndMAp[curr_word] >= (len(word) - i - 1):
            continue
        start = i + 1
        end = len(word) - 1
        isPalin = True
        while start < end:
            if word[start] != word[end]:
                isPalin = False
                break
            start += 1
            end -= 1
        if isPalin:
            palinEndMAp[curr_word] = len(word) - i - 1


def buildPalinStartMap(word, palinStartMap):
    buildPalinEndMap(word[::-1], palinStartMap)


def helper_func(word, trie, startPMap, endPMap):
    temp = trie
    curr_stack = ''
    for i in range(len(word)):
        if temp.isEndOfWord and curr_stack in startPMap and startPMap[curr_stack] > 0:
            return 1
        if temp.children[ord(word[i]) - ord('a')] is None:
            return 0
        curr_stack += word[i]
        temp = temp.children[ord(word[i]) - ord('a')]
    if curr_stack in endPMap and endPMap[curr_stack] > 0:
        return 1
    if len(curr_stack) > 1 and curr_stack in endPMap and curr_stack[::-1] in endPMap and curr_stack[::-1] != curr_stack:
        return 1
    return 0


def search_palindromes(dictionary):
    if len(dictionary) < 2:
        return 0
    trie = trie_search_insert.TrieNode()
    startPMap, endPMap = {}, {}
    for word in dictionary:
        trie_search_insert.Solution.insert(trie, word)
        buildPalinEndMap(word, endPMap)
        buildPalinStartMap(word, startPMap)

    for word in dictionary:
        word = word[::-1]
        if helper_func(word, trie, startPMap, endPMap) == 1:
            return 1
    return 0


if __name__ == "__main__":
    print(search_palindromes(['ge', 'geg']))