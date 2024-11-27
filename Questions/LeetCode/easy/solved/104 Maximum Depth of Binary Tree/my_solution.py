def maxDepth(self, root) -> int:
    count = 0
    if not root:
        return 0
    if not (root.left or root.right):
        return 1
    count += 1
    if not root.left:
        count += self.maxDepth(root.right)
    elif not root.right:
        count += self.maxDepth(root.left)
    else:
        count += max(self.maxDepth(root.left), self.maxDepth(root.right))
    return count