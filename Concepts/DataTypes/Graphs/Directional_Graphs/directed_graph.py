class Graph:

    def __init__(self, edges=None, graph=None):
        self.edges = edges
        self.graph = graph

        if self.graph is None and self.edges is not None:
            self.graph = self.__get_graph()

    def print_graph(self):
        for node, adj_node in self.graph.items():
            print(f"{node}, {adj_node}")

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

    def check_if_path_exists_dfs(self, source, destination):
        stack = [source]
        while len(stack):
            node = stack.pop()
            if node == destination:
                return True
            if node not in self.graph:
                continue
            for adj_node in self.graph[node]:
                stack.append(adj_node)
        return

    def check_if_path_exists_dfs_recursive(self, source, destination):
        if source == destination:
            return True
        if source not in self.graph:
            return False
        for adj_node in self.graph[source]:
            if adj_node in self.graph:
                if self.check_if_path_exists_dfs_recursive(adj_node, destination):
                    return True
        return False

    def check_if_path_exists_bfs(self, source, destination):
        nodes_queue = [source]
        while len(nodes_queue):
            node, nodes_queue = nodes_queue[0], nodes_queue[1:]
            if node == destination:
                return True
            if node in self.graph:
                for adj_node in self.graph[node]:
                    nodes_queue.append(adj_node)
        return False

    def __get_graph(self):
        graph = {}
        for edge in self.edges:
            if edge[0] in graph:
                graph[edge[0]].append(edge[1])
            else:
                graph[edge[0]] = [edge[1]]
        return graph


def main():
    graph_dict = {
        "f": ["i", "g"],
        "g": ["h"],
        "h": [],
        "i": ["g", "k"],
        "j": ["i"],
        "k": []
    }

    graph = Graph(graph=graph_dict)
    # graph.print_graph()
    # print(f"is path exists from 'f' to 'g': {graph.check_if_path_exists_dfs('f', 'g')}")
    # print(f"is path exists from 'f' to 'g': {graph.check_if_path_exists_dfs('j', 'h')}")

    # print(f"is path exists from 'f' to 'g': {graph.check_if_path_exists_dfs_recursive('f', 'k')}")
    # print(f"is path exists from 'f' to 'g': {graph.check_if_path_exists_dfs_recursive('i', 'j')}")

    print(f"is path exists from 'f' to 'g': {graph.check_if_path_exists_bfs('f', 'k')}")
    print(f"is path exists from 'f' to 'g': {graph.check_if_path_exists_bfs('i', 'j')}")


if __name__ == "__main__":
    main()
