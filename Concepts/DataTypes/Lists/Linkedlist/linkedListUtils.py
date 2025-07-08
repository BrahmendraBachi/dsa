from Concepts.DataTypes.Lists.Linkedlist.linkedlist import Node, LinkedList


def merge_sorted_linked_lists(linkedList1, linkedList2):
    # head1, head2 = linkedList1.returnHead(), linkedList2.returnHead()
    head1 = None if linkedList1 is None else linkedList1.returnHead()
    head2 = None if linkedList2 is None else linkedList2.returnHead()
    temp_head = new_head = None
    while head1 or head2:
        if head1 and head2:
            if head1.val < head2.val:
                val = head1.val
                head1 = head1.next
            else:
                val = head2.val
                head2 = head2.next
        elif head1:
            val = head1.val
            head1 = head1.next
        else:
            val = head2.val
            head2 = head2.next
        if new_head is None:
            new_head = Node(val)
            temp_head = new_head
        else:
            temp_head.next = Node(val)
            temp_head = temp_head.next
    new_linked_list = LinkedList(start_head=new_head)
    new_linked_list.print_elements()
    return new_linked_list


def merge_two_linked_lists(linkedList1, linkedList2):
    head1, head2 = linkedList1.returnHead(), linkedList2.returnHead()
    if head1.val > head2.val:
        head1, head2 = head2, head1

    temp1 = head1

    prev = None
    while head1 and head2:
        if head1.val < head2.val:
            prev = head1
            head1 = head1.next
        else:
            prev.next = head2
            temp = head2.next
            head2.next = head1
            prev = head2
            head2 = temp
        if head2:
            prev.next = head2

    return temp1


class LinkedListUtils:
    pass


if __name__ == "__main__":
    sorted_list1 = [1, 3, 8]
    sorted_list2 = [2, 4, 6, 7]

    linked_list1 = LinkedList(sorted_list1)
    linked_list2 = LinkedList(sorted_list2)
    linkedListUtils = LinkedListUtils()
    # merged_linked_list = merge_sorted_linked_lists(linked_list1, linked_list2)
    # merged_linked_list = LinkedList(start_head=merged_linked_list)
    merged_linked_list = merge_two_linked_lists(linked_list1, linked_list2)
    # merged_linked_list.print_elements()
