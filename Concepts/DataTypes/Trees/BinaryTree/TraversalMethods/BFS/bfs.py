from Concepts.DataTypes.Trees.BinaryTree.binary_tree_utils import getSampleBinaryTree


def traverse_bfs(root):

    elements = []
    queue = [root]
    while len(queue):
        root, queue = queue[0], queue[1:]
        elements.append(root.val)
        if root.left:
            queue.append(root.left)
        if root.right:
            queue.append(root.right)

    return elements


if __name__ == "__main__":
    binaryTree = getSampleBinaryTree()
    traversalElements = traverse_bfs(binaryTree)

    print(traversalElements)
