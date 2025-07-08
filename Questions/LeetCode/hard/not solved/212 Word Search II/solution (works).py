from typing import List


def findWords(board: List[List[str]], words: List[str]) -> List[str]:
    n, m = len(board), len(board[0])
    traversed_paths = set()

    def search_in_grid(x, y, ind, search_word):
        if ind == len(search_word):
            return True
        if not (0 <= x < n and 0 <= y < m) or (x, y) in traversed_paths:
            return False

        if board[x][y] != search_word[ind]:
            return False

        traversed_paths.add((x, y))

        is_found = (
                search_in_grid(x, y + 1, ind + 1, search_word) or
                search_in_grid(x, y - 1, ind + 1, search_word) or
                search_in_grid(x + 1, y, ind + 1, search_word) or
                search_in_grid(x - 1, y, ind + 1, search_word)
        )

        traversed_paths.remove((x, y))
        return is_found

    def check_for_word(search_word):
        for i in range(n):
            for j in range(m):
                if search_in_grid(i, j, 0, search_word):
                    return True
        return False

    res = []
    for word in words:
        if check_for_word(word):
            print(traversed_paths)
            res.append(word)

    return res
