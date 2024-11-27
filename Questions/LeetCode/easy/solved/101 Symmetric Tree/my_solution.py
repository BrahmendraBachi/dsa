def isSymmetric(self, root) -> bool:
    return self.checkForSymmetry(root.left, root.right)


def checkForSymmetry(self, leftNode, rightNode):
    if (not leftNode and rightNode) or (not rightNode and leftNode):
        return False

    if not (leftNode and rightNode):
        return True

    return leftNode.val == rightNode.val and self.checkForSymmetry(leftNode.left,
                                                                   rightNode.right) and self.checkForSymmetry(
        leftNode.right, rightNode.left)

# isSymmetric()