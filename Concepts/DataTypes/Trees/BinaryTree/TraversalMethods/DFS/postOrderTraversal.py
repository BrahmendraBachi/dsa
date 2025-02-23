from Concepts.DataTypes.Trees.BinaryTree.binary_tree_utils import getSampleBinaryTree


# order: left, right, root
def postOrderTraversal(root):
    elements = []
    if root.left:
        elements += postOrderTraversal(root.left)
    if root.right:
        elements += postOrderTraversal(root.right)
    elements += [root.val]
    return elements


if __name__ == "__main__":
    binaryTree = getSampleBinaryTree()
    traversalElements = postOrderTraversal(binaryTree)