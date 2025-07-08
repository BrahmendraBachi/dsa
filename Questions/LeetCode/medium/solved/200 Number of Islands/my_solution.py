from typing import List


def numIslands(grid: List[List[str]]) -> int:
    n, m = len(grid), len(grid[0])
    visited = set()

    def dfs(x, y):
        if not (0 <= x < n and 0 <= y < m) or (x, y) in visited or grid[x][y] == "0":
            return 0
        visited.add((x, y))
        dfs(x, y - 1)
        dfs(x, y + 1)
        dfs(x - 1, y)
        dfs(x + 1, y)

        return 1

    count = 0
    for i in range(n):
        for j in range(m):
            count += dfs(i, j)

    return count
