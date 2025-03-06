from typing import List


def exist(board: List[List[str]], word: str) -> bool:
    n, m = len(board), len(board[0])
    traversed_paths = set()

    def search_in_grid(x, y, index):
        if index == len(word):
            return True
        if not (0 <= x < n and 0 <= y < m):
            return False
        if (x, y) in traversed_paths or board[x][y] != word[index]:
            return False

        traversed_paths.add((x, y))

        is_found = (
                search_in_grid(x + 1, y, index + 1) or
                search_in_grid(x - 1, y, index + 1) or
                search_in_grid(x, y + 1, index + 1) or
                search_in_grid(x, y - 1, index + 1)
        )

        traversed_paths.remove((x, y))
        # dp[(x, y, index)] = is_found
        return is_found

    for i in range(n):
        for j in range(m):
            if search_in_grid(i, j, 0):
                return True
    return False
