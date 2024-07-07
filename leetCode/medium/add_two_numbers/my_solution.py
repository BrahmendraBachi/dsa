# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    total = carry = 0

    dummy = ListNode()

    result = dummy
    count = 0

    while l1 or l2 or carry:
        total = carry

        if l1:
            total += l1.val
            l1 = l1.next
        if l2:
            total += l2.val
            l2 = l2.next
        num = total % 10
        dummy.val = num
        carry = total // 10
        # print(carry)
        if l1 or l2 or carry:
            dummy.next = ListNode()
            dummy = dummy.next

    return result