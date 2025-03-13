from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node'], visited=None) -> Optional['Node']:
        if visited is None:
            visited = {}
        if node is None:
            return
        if node.val in visited:
            return visited[node.val]
        visited[node.val] = Node(node.val)
        new_neighbors = []
        for neighbor in node.neighbors:
            new_neighbors.append(self.cloneGraph(neighbor, visited))

        visited[node.val].neighbors = new_neighbors
        return visited[node.val]
