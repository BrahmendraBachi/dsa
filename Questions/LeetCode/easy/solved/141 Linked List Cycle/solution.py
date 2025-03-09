from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    @staticmethod
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        ptr1 = head
        ptr2 = head

        count = 0
        while ptr1:
            ptr1 = ptr1.next
            ptr2 = ptr2.next
            if not ptr2:
                return False
            ptr2 = ptr2.next
            if ptr1.val == ptr2.val:
                return True

        return False
