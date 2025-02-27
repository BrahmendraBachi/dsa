def get_largest_component_count(graph):
    traversed_nodes = set()
    max_count = 0
    for node in graph:
        max_count = max(max_count, traverse_and_count(graph, node, traversed_nodes))
    return max_count


def traverse_and_count(graph, node, traversed_nodes):
    if node in traversed_nodes:
        return 0
    traversed_nodes.add(node)
    count = 1
    for adj_node in graph[node]:
        count += traverse_and_count(graph, adj_node, traversed_nodes)
    return count


def main():
    graph = {
        0: [8, 1, 5],
        1: [0],
        5: [0, 8],
        8: [0, 5],
        2: [3, 4],
        3: [2, 4],
        4: [3, 2]
    }

    # print(get_largest_component_count(graph))
    print(traverse_and_count(graph, 0, set()))


if __name__ == "__main__":
    main()
