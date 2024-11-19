from dsa.Concepts.DataTypes.Trees.BinaryTree.binary_tree_utils import getSampleBinaryTree


def traverse_bfs(root):
    elements = []
    root_nodes = [root]
    while len(root_nodes):
        temp_nodes = []
        for node in root_nodes:
            elements.append(node.val)
            if node.left:
                temp_nodes.append(node.left)
            if node.right:
                temp_nodes.append(node.right)
        root_nodes = temp_nodes
    return elements

if __name__ == "__main__":
    binaryTree = getSampleBinaryTree()
    traversalElements = traverse_bfs(binaryTree)

    print(traversalElements)