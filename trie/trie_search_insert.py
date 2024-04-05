class TrieNode:

    def __init__(self):
        self.children = [None] * 26

        # isEndOfWord is True if node represent the end of the word
        self.isEndOfWord = False


class Solution:
    # Function to insert string into TRIE.
    @staticmethod
    def insert(root, key):
        # code here
        if len(key) == 0:
            return

        if root is None:
            return

        temp = root

        for i in range(0, len(key)):
            if temp.children[ord(key[i]) - ord('a')] is None:
                temp.children[ord(key[i]) - ord('a')] = TrieNode()
            temp = temp.children[ord(key[i]) - ord('a')]

        temp.isEndOfWord = True

    # Function to use TRIE data structure and search the given string.
    @staticmethod
    def search(root, key):

        # code here
        if len(key) == 0:
            return 0

        temp = root

        for i in range(len(key)):
            if temp.children[ord(key[i]) - ord('a')] is None:
                return 0
            temp = temp.children[ord(key[i]) - ord('a')]

        return temp.isEndOfWord
