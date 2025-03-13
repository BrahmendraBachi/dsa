from typing import Optional


class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    @staticmethod
    def cloneGraph(node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None

        visited = {node.val: Node(node.val)}
        queue = [node]

        while queue:
            curr = queue.pop(0)
            for neighbor in curr.neighbors:
                if neighbor.val not in visited:
                    visited[neighbor.val] = Node(neighbor.val)
                    queue.append(neighbor)
                visited[curr.val].neighbors.append(visited[neighbor.val])

        return visited[node.val]
