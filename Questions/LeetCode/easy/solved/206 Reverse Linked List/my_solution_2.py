# Recursive
def reverseList(self, head):
    return self.recursiveReverse(None, head)


def recursiveReverse(self, prev, curr):
    if not curr:
        return prev
    temp = curr.next
    curr.next = prev
    return self.recursiveReverse(curr, temp)
