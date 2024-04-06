# User function Template for python3
# https://www.geeksforgeeks.org/problems/word-boggle-ii--141631/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=bottom_sticky_on_article

class Trie:
    def __init__(self):
        self.isFinal = False
        self.children = [None] * 26

    def insert(self, text):

        temp = self

        for i in range(len(text)):
            if temp.children[ord(text[i]) - ord('A')] is None:
                temp.children[ord(text[i]) - ord('A')] = Trie()
            temp = temp.children[ord(text[i]) - ord('A')]

        temp.isFinal = True

    def delete(self, text):
        def delete_helper(trie, txt, depth):
            if not trie:
                return None
            if depth == len(txt):
                trie.isFinal = True
                return trie if any(trie.children) else None
            trie.children[ord(txt[depth]) - ord('A')] = delete_helper(trie.children[ord(txt[depth]) - ord('A')], txt,
                                                                      depth + 1)
            return trie if any(trie.children) else None

        delete_helper(self, text, 0)


class Solution:
    def wordBoggle(self, board, dictionary):
        # return list of words(str) found in the board
        dict_trie = Trie()

        for word in dictionary:
            dict_trie.insert(word)

        ans = []

        for i in range(len(board)):
            for j in range(len(board[0])):
                self.searchWordsOfDictionary(dict_trie, board, '', (i, j), set(), ans)
                ans = list(set(ans))
                to_deleted = [word for word in dictionary if word in ans]
                for word in to_deleted:
                    dict_trie.delete(word)
                dictionary = [word for word in dictionary if word not in ans]
                if not dictionary:
                    return ans

        return ans

    @staticmethod
    def canMoveThere(trie, next_index, board, visited):
        if next_index in visited:
            return False
        if next_index[0] < 0 or next_index[1] < 0:
            return False
        if next_index[0] >= len(board) or next_index[1] >= len(board[0]):
            return False
        return trie.children[ord(board[next_index[0]][next_index[1]]) - ord('A')] is not None

    def searchThisNextIndex(self, trie, next_index, board, visited, curr_stack, words_found):
        if trie is None:
            return
        if self.canMoveThere(trie, next_index, board, visited):
            self.searchWordsOfDictionary(trie,
                                         board,
                                         curr_stack,
                                         next_index,
                                         visited, words_found)

    # trie is the trie
    # board is the board, ofc
    # curr_stack = the prefix sequence in trie sequence
    # curr_index = curr_index of boggle considered

    def searchWordsOfDictionary(self, trie, board, curr_stack, curr_index, visited, words_found):
        if curr_index in visited:
            return
        if trie is None:
            return
        visited.add(curr_index)
        if trie.children[ord(board[curr_index[0]][curr_index[1]]) - ord('A')] is None:
            return

        curr_stack = curr_stack + board[curr_index[0]][curr_index[1]]

        if trie.children[ord(board[curr_index[0]][curr_index[1]]) - ord('A')].isFinal:
            words_found.append(curr_stack)
            # trie.delete(curr_stack)

        next_index = (curr_index[0], curr_index[1] - 1)
        self.searchThisNextIndex(trie.children[ord(board[curr_index[0]][curr_index[1]]) - ord('A')], next_index, board,
                                 visited, curr_stack, words_found)
        next_index = (curr_index[0], curr_index[1] + 1)
        self.searchThisNextIndex(trie.children[ord(board[curr_index[0]][curr_index[1]]) - ord('A')], next_index, board,
                                 visited, curr_stack, words_found)
        next_index = (curr_index[0] - 1, curr_index[1])
        self.searchThisNextIndex(trie.children[ord(board[curr_index[0]][curr_index[1]]) - ord('A')], next_index, board,
                                 visited, curr_stack, words_found)
        next_index = (curr_index[0] + 1, curr_index[1])
        self.searchThisNextIndex(trie.children[ord(board[curr_index[0]][curr_index[1]]) - ord('A')], next_index, board,
                                 visited, curr_stack, words_found)
        next_index = (curr_index[0] + 1, curr_index[1] - 1)
        self.searchThisNextIndex(trie.children[ord(board[curr_index[0]][curr_index[1]]) - ord('A')], next_index, board,
                                 visited, curr_stack, words_found)
        next_index = (curr_index[0] - 1, curr_index[1] - 1)
        self.searchThisNextIndex(trie.children[ord(board[curr_index[0]][curr_index[1]]) - ord('A')], next_index, board,
                                 visited, curr_stack, words_found)
        next_index = (curr_index[0] + 1, curr_index[1] + 1)
        self.searchThisNextIndex(trie.children[ord(board[curr_index[0]][curr_index[1]]) - ord('A')], next_index, board,
                                 visited, curr_stack, words_found)
        next_index = (curr_index[0] - 1, curr_index[1] + 1)
        self.searchThisNextIndex(trie.children[ord(board[curr_index[0]][curr_index[1]]) - ord('A')], next_index, board,
                                 visited, curr_stack, words_found)
        visited.remove(curr_index)
