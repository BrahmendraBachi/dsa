from dsa.Concepts.DataTypes.Trees.BinaryTree.binary_tree_utils import getSampleBinaryTree


# order: left, root, right
def InOrderTraversal(root):
    elements = []
    if root.left:
        elements += InOrderTraversal(root.left)
    elements += [root.val]
    if root.right:
        elements += InOrderTraversal(root.right)
    return elements


if __name__ == "__main__":
    binaryTree = getSampleBinaryTree()
    traversalElements = InOrderTraversal(binaryTree)
    print(traversalElements)