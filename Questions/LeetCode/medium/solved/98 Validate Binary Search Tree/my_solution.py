class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.prev = None
        self.isValid = True

    def isValidBST(self, root) -> bool:
        if not root:
            return True
        if root.left:
            self.isValidBST(root.left)
        if self.prev is not None and self.prev >= root.val:
            self.isValid = False
        self.prev = root.val
        if root.right:
            self.isValidBST(root.right)
        return self.isValid
