def kthSmallest(self, root, k):
    countAndValue = {"count": 0, "val": None}

    def inOrderTraverse(node):
        if countAndValue["val"]:
            return
        if node.left:
            inOrderTraverse(node.left)
        countAndValue["count"] += 1
        if countAndValue["count"] == k:
            countAndValue["val"] = node.val
            return
        if node.right:
            inOrderTraverse(node.right)
        return

    inOrderTraverse(root)
    return countAndValue["val"]
