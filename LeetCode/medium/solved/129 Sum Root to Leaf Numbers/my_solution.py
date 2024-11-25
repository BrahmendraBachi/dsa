def sumNumbers(self, root) -> int:
    return self.sumOfRootToLeafNode(root)


def sumOfRootToLeafNode(self, root, curr_sum=""):
    if not root:
        return 0
    left_sum = right_sum = 0
    curr_sum += str(root.val)
    if not (root.left or root.right):
        return int(curr_sum)
    if root.left:
        left_sum = self.sumOfRootToLeafNode(root.left, curr_sum)
    if root.right:
        right_sum = self.sumOfRootToLeafNode(root.right, curr_sum)
    return left_sum + right_sum

# sumNumbers(root), i.e., 'root' --> rootNode of binaryTree
