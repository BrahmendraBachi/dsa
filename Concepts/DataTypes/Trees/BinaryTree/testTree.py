from dsa.Concepts.DataTypes.Trees.BinaryTree.binary_tree_utils import Node

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isBST(node, min_val=float('-inf'), max_val=float('inf')):
    if not node:
        return True
    if not (min_val < node.val < max_val):
        return False
    return isBST(node.left, min_val, node.val) and isBST(node.right, node.val, max_val)






if __name__ == "__main__":
    root = TreeNode(10, TreeNode(5), TreeNode(15, TreeNode(12), TreeNode(20)))

    root2 = TreeNode(10, TreeNode(5), TreeNode(15, TreeNode(6), TreeNode(20)))
    print(isBST(root2))

    # print(inOrderTraversal(rootNode))



