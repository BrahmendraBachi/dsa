# Definition for a binary tree node.
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    if not root:
        return []
    res = [[root.val]]

    def traverseAllNodes(roots):
        if len(roots) == 0:
            return
        new_roots = []
        vals = []
        for sub_root in roots:
            if sub_root.left:
                vals.append(sub_root.left.val)
                new_roots.append(sub_root.left)
            if sub_root.right:
                vals.append(sub_root.right.val)
                new_roots.append(sub_root.right)
        if len(vals):
            res.append(vals)
        traverseAllNodes(new_roots)

    traverseAllNodes([root])
    return res
