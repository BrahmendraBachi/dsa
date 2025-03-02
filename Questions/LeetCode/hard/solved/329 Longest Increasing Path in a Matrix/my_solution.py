from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:

        dp = {}
        max_count = 1
        n, m = len(matrix), len(matrix[0])
        for i in range(n):
            for j in range(m):
                count = self.findMaxPathForNode(matrix, i, j, dp)
                print(i, j, count)
                max_count = max(count, max_count)
        return max_count

    def findMaxPathForNode(self, matrix, x, y, dp, parent=float('-inf')):
        hashCode = (x, y)
        if not (0 <= x < len(matrix)) or not (0 <= y < len(matrix[0])) or parent >= matrix[x][y]:
            return 0
        if hashCode in dp:
            return dp[hashCode]
        dp[hashCode] = 1

        left, right, up, down = [x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]

        max_left_length = self.findMaxPathForNode(matrix, left[0], left[1], dp, matrix[x][y])
        max_right_length = self.findMaxPathForNode(matrix, right[0], right[1], dp, matrix[x][y])
        max_up_length = self.findMaxPathForNode(matrix, up[0], up[1], dp, matrix[x][y])
        max_down_length = self.findMaxPathForNode(matrix, down[0], down[1], dp, matrix[x][y])

        dp[hashCode] += max(max_left_length, max_right_length, max_up_length, max_down_length)

        return dp[hashCode]
