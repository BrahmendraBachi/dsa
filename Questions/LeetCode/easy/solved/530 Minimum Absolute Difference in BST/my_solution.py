def getMinimumDifference(self, root):
    minDiff = None
    prevNode = None

    def inOrderTraversal(node):
        nonlocal minDiff, prevNode
        if node.left:
            inOrderTraversal(node.left)
        if prevNode:
            minDiff = abs(node.val - prevNode.val) if minDiff is None else min(minDiff, abs(node.val - prevNode.val))
        prevNode = node
        if node.right:
            inOrderTraversal(node.right)

    inOrderTraversal(root)
    return minDiff