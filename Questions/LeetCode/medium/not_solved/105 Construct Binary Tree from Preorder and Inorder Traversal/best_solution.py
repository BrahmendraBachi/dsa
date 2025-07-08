from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return

        root = TreeNode(preorder[0])
        mid = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:mid + 1], inorder[:mid])
        root.right = self.buildTree(preorder[mid + 1:], inorder[mid + 1:])

        return root

    def print_tree(self, root):
        if root.val:
            print(root.val)
        if root.left:
            self.print_tree(root.left)
        if root.right:
            self.print_tree(root.right)


def main():
    preorder = [1, 2, 4, 5, 3, 6, 7]
    inorder = [4, 2, 1, 5, 6, 3, 7]

    solution = Solution()
    root = solution.buildTree(preorder, inorder)

    # testing the root
    solution.print_tree(root)


if __name__ == "__main__":
    main()
