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
        count = 0
        if not (self.left or self.right):
            count += 1
        elif not self.right:
            count += self.left.countLeafNodes()
        elif not self.left:
            count += self.right.countLeafNodes()
        else:
            count += self.left.countLeafNodes() + self.right.countLeafNodes()
        return count

    def getMaxDepth(self):
        count = 0
        if not (self.left or self.right):
            return 0
        count += 1
        if not self.right:
            count += self.left.getMaxDepth()
        elif not self.left:
            count += self.right.getMaxDepth()
        else:
            count += max(self.left.getMaxDepth(), self.right.getMaxDepth())
        return count






def main():

    binaryTree = prepareBinaryTree()
    print(binaryTree.countLeafNodes())

    print(binaryTree.getMaxDepth())

if __name__ == "__main__":
    main()