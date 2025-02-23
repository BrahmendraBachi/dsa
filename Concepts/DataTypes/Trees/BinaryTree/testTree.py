from Concepts.DataTypes.Trees.BinaryTree.binary_tree_utils import Node


def flatten(root):
    left = right = None
    if root.left:
        left = flatten(root.left)
    if root.right:
        right = flatten(root.right)

    temp = root
    if left:
        temp.right = left
        while temp.right:
            temp = temp.right
    if right:
        temp.right = right
    root.left = None
    return root


if __name__ == "__main__":
    rootNode = Node(1)

    node2 = Node(2)
    node5 = Node(5)

    rootNode.left = node2
    rootNode.right = node5

    node3 = Node(3)
    node4 = Node(4)

    node2.left = node3
    node2.right = node4

    node6 = Node(6)
    node5.right = node6

    flattenRoot = flatten(rootNode)
    print(flattenRoot)
    while flattenRoot:
        print(flattenRoot.val)
        flattenRoot = flattenRoot.right

    # print(inOrderTraversal(rootNode))
