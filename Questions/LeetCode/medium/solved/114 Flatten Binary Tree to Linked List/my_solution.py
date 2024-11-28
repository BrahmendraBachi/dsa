def flatten(self, root):
    leftFlatten = rightFlatten = None
    if root is None:
        return None
    if root.left:
        leftFlatten = self.flatten(root.left)
    if root.right:
        rightFlatten = self.flatten(root.right)

    temp = root
    if leftFlatten:
        temp.right = leftFlatten
        while temp.right:
            temp = temp.right
    if rightFlatten:
        temp.right = rightFlatten
    root.left = None
    return root