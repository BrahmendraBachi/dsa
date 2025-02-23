from typing import List


def spiralOrder(matrix: List[List[int]]) -> List[int]:
    result = []
    starts = [0, 0]
    n, m = len(matrix), len(matrix[0])
    ends = [n - 1, m - 1]
    count = 0
    while count <= min(n, m) // 2:
        a, b = starts[1], ends[1] + 1
        for i in range(a, b):
            result.append(matrix[starts[0]][i])
            if len(result) >= n * m:
                return result

        starts[0] += 1
        a, b = starts[0], ends[0] + 1
        for i in range(a, b):
            result.append(matrix[i][ends[1]])
            if len(result) >= n * m:
                return result

        ends[1] -= 1
        a, b = ends[1], starts[1]
        for i in range(a, b - 1, -1):
            result.append(matrix[ends[0]][i])
            if len(result) >= n * m:
                return result

        ends[0] -= 1
        a, b = ends[0], starts[0]
        for i in range(a, b - 1, -1):
            result.append(matrix[i][starts[1]])
            if len(result) >= n * m:
                return result
        starts[1] += 1
        count += 1

    return result
