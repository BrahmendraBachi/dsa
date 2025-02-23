from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        return self.maxPattern(grid, n, m)

    def maxPattern(self, grid, n, m, x=0, y=0, count1=0):
        if grid[x][y] == 1:
            count1 = max(self.findPattern(grid, n, m, x, y, 0), count1)
        if y < m - 1:
            y += 1
        elif y == m - 1 and x < n - 1:
            y = 0
            x += 1
        else:
            return count1
        return self.maxPattern(grid, n, m, x, y, count1)

    def findPattern(self, grid, n, m, x, y, v=0):
        if not self.checkVaid(n, m, x, y, grid, v):
            return 0
        grid[x][y] = 0
        c = 1 + self.findPattern(grid, n, m, x, y - 1, 1) + self.findPattern(grid, n, m, x, y + 1, 1) \
            + self.findPattern(grid, n, m, x - 1, y, 1) + self.findPattern(grid, n, m, x + 1, y, 1)
        return c

    @staticmethod
    def checkVaid(n, m, x, y, grid, v):
        if (v == 1) and (x < 0 or y < 0 or x >= n or y >= m or grid[x][y] == 0):
            return False
        return True
