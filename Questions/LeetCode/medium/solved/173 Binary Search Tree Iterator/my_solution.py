from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.elements = self.in_order_traversal(root)

    def in_order_traversal(self, root):
        elements = []
        if root.right:
            elements += self.in_order_traversal(root.right)
        elements += [root.val]
        if root.left:
            elements += self.in_order_traversal(root.left)

        return elements

    def next(self) -> int:
        return self.elements.pop()

    def hasNext(self) -> bool:
        return not not len(self.elements)

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
