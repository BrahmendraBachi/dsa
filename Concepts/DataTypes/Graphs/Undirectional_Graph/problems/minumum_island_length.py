def minimum_island_length(grid):
    min_count = float('inf')
    traversed_nodes = set()
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            count = count_island_length(grid, i, j, traversed_nodes)
            if count != 0:
                min_count = min(min_count, count)
    return 0 if min_count == float('-inf') else min_count


def count_island_length(grid, x, y, visited):
    if (not 0 <= x < len(grid)) or (not 0 <= y < len(grid[0])) or grid[x][y] == 'W' or str(x) + "," + str(y) in visited:
        return 0
    visited.add(str(x) + "," + str(y))
    nodes = [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]
    count = 1
    for node in nodes:
        count += count_island_length(grid, node[0], node[1], visited)
    return count


def main():
    grid = [
        ['W', 'L', 'W', 'W', 'W'],
        ['W', 'L', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'L', 'W'],
        ['W', 'W', 'L', 'L', 'W'],
        ['L', 'W', 'W', 'L', 'L'],
        ['L', 'L', 'W', 'W', 'W'],
    ]

    print(minimum_island_length(grid))


if __name__ == "__main__":
    main()
