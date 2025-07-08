def uniquePaths(m: int, n: int) -> int:
    dp = {}

    def dfs(x, y):

        if (x, y) in dp:
            return dp[(x, y)]

        if not (0 <= x < m and 0 <= y < n):
            return 0
        if x == m - 1 and y == n - 1:
            return 1
        dp[(x, y)] = dfs(x + 1, y) + dfs(x, y + 1)

        return dp[(x, y)]

    return dfs(0, 0)
