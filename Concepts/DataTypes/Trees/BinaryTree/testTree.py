from dsa.Concepts.DataTypes.Trees.BinaryTree.binary_tree_utils import Node

def sumOfRootToLeafNode(treeNode, curr_sum = ""):
    if not treeNode:
        return 0
    left_sum = right_sum = 0
    curr_sum = curr_sum + str(treeNode.val)
    if not (treeNode.left or treeNode.right):
        return int(curr_sum)
    if treeNode.left:
        left_sum = sumOfRootToLeafNode(treeNode.left, curr_sum)
    if treeNode.right:
        right_sum = sumOfRootToLeafNode(treeNode.right, curr_sum)
    return left_sum + right_sum


if __name__ == "__main__":
    # binarySearchTree = generateBinarySearchTree([2, 1, 3])
    # binaryTree = generateBinarySearchTree([4, 9, 0, 5, 1])
    rootNode = Node(4)

    node1 = Node(9)
    node2 = Node(0)

    node3 = Node(5)
    node4 = Node(1)

    rootNode.left = node1
    rootNode.right = node2

    node1.left = node3
    node1.right = node4
    print(sumOfRootToLeafNode(rootNode))

