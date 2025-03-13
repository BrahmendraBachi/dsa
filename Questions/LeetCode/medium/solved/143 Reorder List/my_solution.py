from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    next_half = None
    prev = None

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        n = 0

        def dfs(curr_ind, curr_node):

            if curr_ind == n // 2:
                if n % 2 == 0:
                    self.next_half = curr_node
                    self.prev.next = None
                else:
                    self.next_half = curr_node.next
                    curr_node.next = None
                return
            self.prev = curr_node
            dfs(curr_ind + 1, curr_node.next)
            next_node = self.next_half
            next_half = next_node.next
            next_node.next = None
            curr_node_next = curr_node.next
            curr_node.next = self.next_half
            next_node.next = curr_node_next
            self.next_half = next_half

        start = head
        while start:
            n += 1
            start = start.next

        dfs(0, head)

        return head
