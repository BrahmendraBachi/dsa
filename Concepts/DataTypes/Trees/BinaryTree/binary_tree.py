from binary_tree_utils import Node


def prepareBinaryTree():
    rootNode = BinaryTree('R')
    nodeA = BinaryTree('A')
    nodeB = BinaryTree('B')
    nodeC = BinaryTree('C')
    nodeD = BinaryTree('D')
    nodeE = BinaryTree('E')
    nodeF = BinaryTree('F')
    nodeG = BinaryTree('G')

    rootNode.left = nodeA
    rootNode.right = nodeB

    nodeA.left = nodeC
    nodeA.right = nodeD

    nodeB.left = nodeE
    nodeB.right = nodeF

    nodeF.left = nodeG

    return rootNode


class BinaryTree(Node):

    def countLeafNodes(self):
        if not self.left and not self.right:
            return 1
        count = 0
        if self.left:
            count += self.left.countLeafNodes()
        if self.right:
            count += self.right.countLeafNodes()

        return count

    def getMaxDepth(self):
        if not self.left and not self.right:
            return 1

        left = right = 0
        if self.left:
            left = self.left.getMaxDepth()
        if self.right:
            right = self.right.getMaxDepth()

        return 1 + max(left, right)


def main():
    binaryTree = prepareBinaryTree()
    print(binaryTree.countLeafNodes())

    print(binaryTree.getMaxDepth())


if __name__ == "__main__":
    main()
