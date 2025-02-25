class Graph:

    def __init__(self, edges=None):
        self.edges = edges
        self.graph = self.__get_graph()

    def print_graph(self):
        for node, adj_nodes in self.graph.items():
            print(f"{node}, {adj_nodes}")

    def dfs(self, source):
        stack = [source]
        while len(stack):
            node = stack.pop()
            print(node, end=", ")
            if node in self.graph:
                for adj_node in self.graph[node]:
                    stack.append(adj_node)

    def dfs_recursive(self, source):
        print(source, end=", ")
        if source not in self.graph:
            return
        for adj_node in self.graph[source]:
            self.dfs_recursive(adj_node)

    def bfs(self, source):
        graph_queue = [source]
        while len(graph_queue):
            node, graph_queue = graph_queue[0], graph_queue[1:]
            print(node, end=", ")
            if node in self.graph:
                for adj_node in self.graph[node]:
                    graph_queue.append(adj_node)




    def __get_graph(self):
        graph = {}
        for edge in self.edges:
            if edge[0] in graph:
                graph[edge[0]].append(edge[1])
            else:
                graph[edge[0]] = [edge[1]]
        return graph


def main():
    edges = [
        ("a", "b"),
        ("a", "c"),
        ("c", "e"),
        ("b", "d"),
        ("f", "d")
    ]

    graph = Graph(edges)
    # graph.print_graph()

    # DFS
    graph.dfs("a")
    print()
    graph.dfs_recursive("a")
    print()

    graph.bfs("a")




if __name__ == "__main__":
    main()
