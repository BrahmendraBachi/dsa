from Concepts.DataTypes.Graphs.Undirectional_Graph.undirected_graph import Undirected_Graph


def connected_components_count(graph):
    all_nodes = graph.keys()
    traversed_nodes = set()
    count = 0
    for node in all_nodes:
        count += traverse_from_node(graph, node, traversed_nodes)
    return count


def traverse_from_node(graph, node, traversed_nodes):
    if node in traversed_nodes or node not in graph:
        return 0
    traversed_nodes.add(node)
    for adj_node in graph[node]:
        traverse_from_node(graph, adj_node, traversed_nodes)
    return 1


def main():
    graph = {
        3: [],
        4: [6],
        6: [4, 5, 7, 8],
        8: [6],
        7: [6],
        5: [6],
        1: [2],
        2: [1]
    }

    print(connected_components_count(graph))


if __name__ == "__main__":
    main()
