def shortest_path(graph, source, destination, path=None):
    if path is None:
        path = set()
    path.add(source)
    if source == destination:
        return path
    if source not in graph:
        return []
    min_path_count = float('-inf')
    for adj_node in graph[source]:
        if adj_node not in path:
            s_path = shortest_path(graph, adj_node, destination, path)


def main():
    pass


if __name__ == "__main__":
    main()
