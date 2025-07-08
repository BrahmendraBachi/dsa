from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        dp = {}
        n = len(matrix)
        m = len(matrix[0])
        max_area = 0
        for i in range(n):
            for j in range(m):
                length = self.find_max_square(matrix, i, j, dp)
                max_area = max(length * length, max_area)
        return max_area

    def find_max_square(self, matrix, x, y, dp):
        if not (0 <= x < len(matrix)) or not (0 <= y < len(matrix[0])) or matrix[x][y] == "0":
            return 0

        if (x, y) in dp:
            return dp[(x, y)]

        right = self.find_max_square(matrix, x, y + 1, dp)
        down = self.find_max_square(matrix, x + 1, y, dp)
        diagonal = self.find_max_square(matrix, x + 1, y + 1, dp)

        dp[(x, y)] = 1 + min(right, down, diagonal)

        return dp[(x, y)]
