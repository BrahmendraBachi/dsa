from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    ptr1, ptr2 = head, None
    for node in range(n - 1):
        ptr1 = ptr1.next
    ptr2, prev = head, None

    while True:
        if ptr1.next:
            prev = ptr2
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        else:
            if ptr2 == head:
                return head.next
            prev.next = ptr2.next
            break
    return head
