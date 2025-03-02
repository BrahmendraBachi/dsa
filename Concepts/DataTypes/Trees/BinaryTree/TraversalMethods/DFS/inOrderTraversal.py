from Concepts.DataTypes.Trees.BinaryTree.binary_tree_utils import getSampleBinaryTree


# order: left, root, right
def inOrderTraversal(root):
    elements = []
    if root.left:
        elements += inOrderTraversal(root.left)
    elements += [root.val]
    if root.right:
        elements += inOrderTraversal(root.right)
    return elements


def inOrderTraversalIterative(root):
    stack = []
    elements = []
    while root or len(stack):
        while root:
            stack.append(root)
            root = root
            root = root.left
        root = stack.pop()
        elements.append(root.val)
        root = root.right

    return elements


if __name__ == "__main__":
    binaryTree = getSampleBinaryTree()
    traversalElements = inOrderTraversal(binaryTree)
    # print(traversalElements)
    print(inOrderTraversalIterative(binaryTree))
