from dsa.concepts.linkedlist.linkedlist import LinkedList

def swapNodesInPairs(linkedList: LinkedList):
    head = linkedList.returnHead()
    if head is None or head.next is None:
        return head
    ptr1 = head
    start_head = ptr2 = head.next
    prev = None
    recursivelySwapNodes(prev, ptr1, ptr2)
    return start_head

def recursivelySwapNodes(prev, ptr1, ptr2):
    if not (ptr1 and ptr2):
        return
    temp = ptr2.next
    ptr2.next = ptr1
    ptr1.next = temp
    if prev:
        prev.next = ptr2
    prev = ptr1
    ptr1 = ptr1.next
    if ptr1:
        ptr2 = ptr1.next
    return recursivelySwapNodes(prev, ptr1, ptr2)

if __name__ == "__main__":
    linkedList1 = LinkedList([1, 2, 3, 4, 5, 6])
    node = swapNodesInPairs(linkedList1)
    LinkedList(start_head=node).print_elements()