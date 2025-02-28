def shortest_path_length(graph, source, destination, path=None):
    if path is None:
        path = set()
    path.add(source)
    if source == destination:
        return len(path) - 1
    if source not in graph:
        return None
    min_path_count = float('inf')
    for adj_node in graph[source]:
        if adj_node not in path:
            s_path_count = shortest_path_length(graph, adj_node, destination, path.copy())
            if s_path_count and s_path_count < min_path_count:
                min_path_count = s_path_count
    return min_path_count


def shortest_path_length_bfs(graph, source, destination):
    traversal_queue = [(source, 0)]
    traversed_paths = set()
    while len(traversal_queue):
        node, distance, traversal_queue = traversal_queue[0][0], traversal_queue[0][1], traversal_queue[1:]
        if node == destination:
            return distance
        if node in traversed_paths:
            continue
        traversed_paths.add(node)
        for adj_node in graph[node]:
            traversal_queue.append((adj_node, distance + 1))
    return -1


def main():
    graph = {
        "w": ["x", "v"],
        "x": ["w", "y"],
        "y": ["x", "z"],
        "z": ["y", "v"],
        "v": ["z", "w"]
    }

    # print(shortest_path_length(graph, "w", "z"))
    # print(shortest_path_length(graph, "w", "v"))
    # print(shortest_path_length(graph, "x", "w"))

    print(shortest_path_length_bfs(graph, "w", "z"))
    print(shortest_path_length_bfs(graph, "w", "v"))
    print(shortest_path_length_bfs(graph, "x", "w"))


if __name__ == "__main__":
    main()
