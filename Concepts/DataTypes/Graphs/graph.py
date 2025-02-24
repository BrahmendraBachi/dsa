class Graph:

    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for edge in self.edges:
            if edge[0] in self.graph_dict:
                self.graph_dict[edge[0]].append((edge[1], edge[2]))
            else:
                self.graph_dict[edge[0]] = [(edge[1], edge[2])]

    def find_all_paths(self, start, end, path=None):
        if path is None:
            path = []
        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph_dict:
            return []
        all_paths = []
        for node in self.graph_dict[start]:
            paths = self.find_all_paths(node[0], end, path)
            all_paths += paths
        return all_paths

    def find_min_nodes_path(self, start, end, path=None):
        if path is None:
            path = []
        path = path + [start]
        if start == end:
            return path
        min_path = None
        for node in self.graph_dict[start]:
            s_path = self.find_min_nodes_path(node[0], end, path)
            if s_path is None:
                continue
            if min_path is None or len(s_path) < len(min_path):
                min_path = s_path
        return min_path

    def find_min_dist(self, start, end, distance=0):
        if start == end:
            return distance

        min_distance = float('inf')
        for node in self.graph_dict[start]:
            min_dist = self.find_min_dist(node[0], end, distance + node[1])
            min_distance = min(min_distance, min_dist)
        return min_distance

    def find_max_dist(self, start, end, distance=0):
        if start == end:
            return distance
        max_distance = float('-inf')
        for node in self.graph_dict[start]:
            max_dist = self.find_max_dist(node[0], end, distance + node[1])
            max_distance = max(max_distance, max_dist)
        return max_distance

    def find_min_distance_path(self, start, end, path=None, distance=0):
        if path is None:
            path = []
        path = path + [start]
        if start == end:
            return distance, path
        min_distance = float('inf')
        min_distance_path = None
        for node in self.graph_dict[start]:
            min_dist, min_path = self.find_min_distance_path(node[0], end, path, distance + node[1])
            if min_path is not None:
                if min_distance_path is None or min_dist < min_distance:
                    min_distance_path = min_path
                    min_distance = min_dist
        return min_distance, min_distance_path

    def find_max_distance_path(self, start, end, path=None, distance=0):
        if path is None:
            path = []
        path = path + [start]
        if start == end:
            return distance, path
        max_distance = float('-inf')
        max_distance_path = None
        for node in self.graph_dict[start]:
            max_dist, max_path = self.find_max_distance_path(node[0], end, path, distance + node[1])
            if max_dist is not None:
                if max_distance_path is None or max_distance < max_dist:
                    max_distance = max_dist
                    max_distance_path = max_path
        return max_distance, max_distance_path


def main():
    routes = [
        ("Mumbai", "Paris", 6),
        ("Mumbai", "Dubai", 10),
        ("Paris", "Dubai", 2),
        ("Paris", "New York", 9),
        ("Dubai", "New York", 1),
        ("New York", "Toronto", 10)
    ]

    graph = Graph(routes)
    all_paths = graph.find_all_paths(start="Mumbai", end="Toronto")
    print("all_paths:")
    print(all_paths)

    min_nodes_path = graph.find_min_nodes_path(start="Mumbai", end="New York")
    print(min_nodes_path)

    min_distance = graph.find_min_dist(start="Mumbai", end="New York")
    print(min_distance)

    max_distance = graph.find_max_dist(start="Mumbai", end="New York")
    print(max_distance)

    min_distance_path = graph.find_min_distance_path("Mumbai", "New York")
    print(min_distance_path)

    max_distance_path = graph.find_max_distance_path("Mumbai", "New York")
    print(max_distance_path)


if __name__ == "__main__":
    main()
