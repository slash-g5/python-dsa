import trie_search_insert

# historical_input = ['apple', 'ape', 'alphabet', 'aqua', 'drrfg', 'yo', 'yoo']

searchTrie = trie_search_insert.TrieNode()


def generateStrings(trie):
    ans = []

    for i in range(26):
        if trie.children[i] is not None:
            if trie.children[i].isEndOfWord:
                ans.append(str(chr(i + ord('a'))))
            next_ans = generateStrings(trie.children[i])
            for na in next_ans:
                ans.append(str(chr(i + ord('a'))) + na)

    return ans


def autoComplete(text, trie):
    ans = []
    if len(text) < 2:
        return ans
    if trie is None:
        return ans

    temp = trie

    for i in range(len(text)):
        if temp.children[ord(text[i]) - ord('a')] is None:
            return ans
        temp = temp.children[ord(text[i]) - ord('a')]

    if temp.isEndOfWord:
        ans.append(text)

    for i in range(26):
        if temp.children[i] is not None:
            if temp.children[i].isEndOfWord:
                ans.append(text + str(chr(i + ord('a'))))
            next_ans = generateStrings(temp.children[i])
            for na in next_ans:
                ans.append(text + str(chr(i + ord('a'))) + na)

    return ans


while True:
    search_text = input()
    print(f"recommendations {autoComplete(search_text, searchTrie)}")

    trie_search_insert.Solution.insert(searchTrie, search_text)
