from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    @staticmethod
    def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:

        start = second_start = head
        while n > 0 and start:
            start = start.next
            n -= 1

        prev = None
        while start:
            prev = second_start
            start = start.next
            second_start = second_start.next

        if prev is None:
            return head.next
        prev.next = second_start.next

        return head
