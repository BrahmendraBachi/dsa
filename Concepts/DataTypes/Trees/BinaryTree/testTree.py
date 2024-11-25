from dsa.Concepts.DataTypes.Trees.BinaryTree.TraversalMethods.BFS.bfs import traverse_bfs
from dsa.Concepts.DataTypes.Trees.BinaryTree.binary_tree_utils import Node
from dsa.LeetCode.easy.solved.valid_paranthesis.my_solution import isValid


def isValidBST(root):
    if not root or not (root.left or root.right):
        return True
    left_side = right_side = True
    if root.left:
        left_side = root.left.val < root.val and isValidBST(root.left)
    if root.right:
        right_side = root.right.val > root.val and isValidBST(root.right)
    return left_side and right_side
if __name__ == "__main__":
    rootNode = Node(5)

    node1 = Node(4)
    node2 = Node(6)
    node3 = Node(3)
    node4 = Node(7)

    rootNode.left = node1
    rootNode.right = node2
    node2.left = node3
    node3.right = node4

    # print(traverse_bfs(rootNode))

    isValidBST(rootNode)


