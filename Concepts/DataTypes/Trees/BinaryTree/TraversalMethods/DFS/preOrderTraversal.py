from Concepts.DataTypes.Trees.BinaryTree.binary_tree_utils import getSampleBinaryTree


# order: root, left, right
def preOrderTraversal(root):
    elements = []
    if root:
        elements = [root.val]
    if root.left:
        elements += preOrderTraversal(root.left)
    if root.right:
        elements += preOrderTraversal(root.right)
    return elements


if __name__ == "__main__":
    binaryTree = getSampleBinaryTree()
    treeElements = preOrderTraversal(binaryTree)

    print(treeElements)
