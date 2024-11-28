def isSameTree(self, p, q) -> bool:
    return (
                (p == q)
                or not (not p or not q)
                and (p.val == q.val)
                and self.isSameTree(p.left, q.left)
                and self.isSameTree(p.right, q.right)
            )