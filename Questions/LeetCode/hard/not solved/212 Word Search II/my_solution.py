from typing import List


class Trie:
    def __init__(self):
        self.children = {}
        self.is_end = False

    def insert_word(self, word):
        root = self
        for ch in word:
            if ch not in root.children:
                root.children[ch] = Trie()
            root = root.children[ch]
        root.is_end = True


def findWords(board: List[List[str]], words: List[str]) -> List[str]:

    n, m = len(board), len(board[0])
    trie = Trie()
    for word in words:
        trie.insert_word(word)

    res, visited = set(), set()

    def dfs(x, y, curr_word, curr_trie):
        if (not (0 <= x < n and 0 <= y < m)) or (x, y) in visited or board[x][y] not in curr_trie.children:
            return

        curr_word += board[x][y]
        curr_trie = curr_trie.children[board[x][y]]
        if curr_trie.is_end:
            res.add(curr_word)

        visited.add((x, y))

        dfs(x, y - 1, curr_word, curr_trie)
        dfs(x, y + 1, curr_word, curr_trie)
        dfs(x - 1, y, curr_word, curr_trie)
        dfs(x + 1, y, curr_word, curr_trie)

        visited.remove((x, y))

    for i in range(n):
        for j in range(m):
            dfs(i, j, "", trie)

    return list(res)
