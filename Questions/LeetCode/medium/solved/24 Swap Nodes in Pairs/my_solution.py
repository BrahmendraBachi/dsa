from Concepts.DataTypes.Lists.Linkedlist.linkedlist import LinkedList


def swapNodesInPairs(linkedList: LinkedList):
    linkedList.print_elements()
    ptr1 = linkedList.head
    ptr2 = linkedList.head.next
    start_node = ptr2
    prev = None
    while ptr2:
        temp = ptr2.next
        ptr2.next = ptr1
        ptr1.next = temp
        if prev:
            prev.next = ptr2
        prev = ptr1
        ptr1 = ptr1.next
        if ptr1 is not None:
            ptr2 = ptr1.next
        else:
            break
    return start_node


if __name__ == "__main__":
    linkedList1 = LinkedList([1, 2, 3, 4, 5, 6])
    node = swapNodesInPairs(linkedList1)
    LinkedList(start_head=node).print_elements()
