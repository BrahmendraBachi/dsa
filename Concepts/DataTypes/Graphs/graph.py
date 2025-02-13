from os.path import pathsep


class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        self.all_paths = []
        for start, end in edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]

    def return_edges_graph(self):
        return self.graph_dict

    def get_all_paths(self, start="Mumbai", end="New York", path=None):
        if path is None:
            path = []
        if start not in self.graph_dict:
            return []
        path = path + [start]
        if start == end:
            return [path]
        all_paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                all_paths += self.get_all_paths(node, end, path)
        return all_paths

    def get_shortest_path(self, start="Mumbai", end="New York", path=None):
        if path is None:
            path = []
        path = path + [start]
        if start == end:
            return path
        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_shortest_path(node, end, path)
                if sp and (shortest_path is None or len(shortest_path) > len(sp)):
                    shortest_path = sp
        return shortest_path



if __name__ == "__main__":
    _edges = [
        ("Mumbai", "Paris"),
        ("Mumbai", "Dubai"),
        ("Paris", "Dubai"),
        ("Paris", "New York"),
        ("Dubai", "New York"),
        ("New York", "Toronto")
    ]

    graph = Graph(_edges)
    print(graph.return_edges_graph())
    print(graph.get_all_paths())

    print(graph.get_shortest_path())