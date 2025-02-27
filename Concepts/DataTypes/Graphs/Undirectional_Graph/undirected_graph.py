class Undirected_Graph:

    def __init__(self, edges=None, graph=None):
        self.edges = edges
        self.graph = graph

        if not self.graph and self.edges:
            self.graph = self.__get_graph()

    def bfs(self, source):
        traversal_queue = [source]
        traversed_nodes = set()
        while len(traversal_queue):
            node, traversal_queue = traversal_queue[0], traversal_queue[1:]
            if node in traversed_nodes or node not in self.graph:
                continue
            print(node)
            traversed_nodes.add(node)
            for adj_nodes in self.graph[node]:
                traversal_queue.append(adj_nodes)

    def dfs(self, source):
        traversal_stack = [source]
        traversed_nodes = set()
        while len(traversal_stack):
            node = traversal_stack.pop()
            if node in traversed_nodes or node not in self.graph:
                continue
            print(node)
            traversed_nodes.add(node)
            for adj_node in self.graph[node]:
                traversal_stack.append(adj_node)

    def dfs_recursive(self, source, traversed_nodes=None):
        if traversed_nodes is None:
            traversed_nodes = set()
        if source in traversed_nodes or source not in self.graph:
            return
        print(source)
        traversed_nodes.add(source)
        for adj_node in self.graph[source]:
            self.dfs_recursive(adj_node, traversed_nodes)

    def check_if_path_exists_bfs(self, source, destination):
        traversal_queue = [source]
        traversed_nodes = set()
        while len(traversal_queue):
            node, traversal_queue = traversal_queue[0], traversal_queue[1:]
            if node == destination:
                return True
            if node in traversed_nodes or node not in self.graph:
                continue
            traversed_nodes.add(node)
            for adj_node in self.graph[node]:
                traversal_queue.append(adj_node)
        return False

    def check_if_path_exists_dfs(self, source, destination):
        traversal_stack = [source]
        traversed_nodes = set()
        while len(traversal_stack):
            node = traversal_stack.pop()
            if node == destination:
                return True
            if node in traversed_nodes or node not in self.graph:
                continue
            traversed_nodes.add(node)
            for adj_node in self.graph[node]:
                traversal_stack.append(adj_node)

        return False

    def check_if_path_exists_dfs_recursive(self, source, destination, traversed_nodes=None):
        if traversed_nodes is None:
            traversed_nodes = set()
        if source == destination:
            return True
        if source in self.graph and source not in traversed_nodes:
            traversed_nodes.add(source)
            for adj_node in self.graph[source]:
                if self.check_if_path_exists_dfs_recursive(adj_node, destination, traversed_nodes):
                    return True
        return False


    def print_graph(self):
        for node, adj_nodes in self.graph.items():
            print(node, adj_nodes)

    def __get_graph(self):
        graph = {}
        for edge in self.edges:
            self.__add_edge(edge[0], edge[1], graph)
            self.__add_edge(edge[1], edge[0], graph)
        return graph

    @staticmethod
    def __add_edge(start, end, graph):
        if start in graph:
            graph[start].append(end)
        else:
            graph[start] = [end]


def main():
    edges = [
        ("i", "j"),
        ("i", "k"),
        ("k", "m"),
        ("k", "j"),
        ("k", "l"),
        ("o", "n")
    ]
    graph = Undirected_Graph(edges=edges)
    graph.print_graph()

    # graph.bfs("i")
    # graph.dfs("i")
    # graph.dfs_recursive("i")

    # print(graph.check_if_path_exists_bfs("i", "l"))
    # print(graph.check_if_path_exists_bfs("i", "m"))
    # print(graph.check_if_path_exists_bfs("i", "o"))

    # print(graph.check_if_path_exists_dfs("i", "l"))
    # print(graph.check_if_path_exists_dfs("i", "m"))
    # print(graph.check_if_path_exists_dfs("i", "o"))

    print(graph.check_if_path_exists_dfs_recursive("i", "l"))
    print(graph.check_if_path_exists_dfs_recursive("i", "m"))
    print(graph.check_if_path_exists_dfs_recursive("i", "o"))



if __name__ == "__main__":
    main()
