from dsa.Concepts.DataTypes.Trees.BinaryTree.binary_tree_utils import Node
from dsa.Concepts.DataTypes.Trees.BinaryTree.TraversalMethods.DFS.inOrderTraversal import inOrderTraversal


def getKthSmallestElement(root, k):
    countAndValue = {"count": 0, "val": None}
    def traverseInOrder(node):
        if countAndValue["val"]:
            return
        if node.left:
            traverseInOrder(node.left)
        countAndValue["count"] += 1
        if countAndValue["count"] == k:
            countAndValue["val"] = node.val
            return
        if node.right:
            traverseInOrder(node.right)
    traverseInOrder(root)
    return countAndValue["val"]
if __name__ == "__main__":
    rootNode = Node(5)

    node3 = Node(3)
    node6 = Node(6)

    rootNode.left = node3
    rootNode.right = node6

    node2 = Node(2)
    node4 = Node(4)

    node3.left = node2
    node3.right = node4

    node1 = Node(1)

    node2.left = Node(1)

    print(getKthSmallestElement(rootNode, 4))
    # print(inOrderTraversal(rootNode))



