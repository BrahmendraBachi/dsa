def island_count(grid):
    traversed_nodes = set()
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            count += checkForIsland(grid, i, j, traversed_nodes)
    return count


def checkForIsland(grid, x, y, visited):
    if (not 0 <= x < len(grid)) or (not 0 <= y < len(grid[0])) or grid[x][y] == 'W' or str(x) + "," + str(y) in visited:
        return 0
    visited.add(str(x) + "," + str(y))
    nodes = [[x, y - 1], [x, y + 1], [x - 1, y], [x + 1, y]]
    for node in nodes:
        checkForIsland(grid, node[0], node[1], visited)
    return 1


def main():
    grid = [
        ['W', 'L', 'W', 'W', 'W'],
        ['W', 'L', 'W', 'W', 'W'],
        ['W', 'W', 'W', 'L', 'W'],
        ['W', 'W', 'L', 'L', 'W'],
        ['L', 'W', 'W', 'L', 'L'],
        ['L', 'L', 'W', 'W', 'W'],
    ]

    print(island_count(grid))


if __name__ == "__main__":
    main()
