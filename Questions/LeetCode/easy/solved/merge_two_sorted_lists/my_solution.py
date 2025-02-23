from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    merged_arr = []
    while True:
        num1, num2 = None, None
        if list1:
            num1 = list1.val
        if list2:
            num2 = list2.val

        if (num1 is not None) and (num2 is not None):
            if num1 < num2:
                merged_arr.append(num1)
                list1 = list1.next
            else:
                merged_arr.append(num2)
                list2 = list2.next

        elif num1 is not None:
            merged_arr.append(num1)
            list1 = list1.next

        elif num2 is not None:
            merged_arr.append(num2)
            list2 = list2.next

        else:
            break

    if not len(merged_arr):
        return None
    head = ListNode(merged_arr[0])
    temp_head = head
    for num in merged_arr[1:]:
        new_node = ListNode(num)
        temp_head.next = new_node
        temp_head = temp_head.next
    return head
