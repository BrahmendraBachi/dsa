from dsa.concepts.linkedlist.linkedlist import LinkedList

def reverseNodesInKGroups(linkedList: LinkedList, k: int):
    n = linkedList.get_length()
    head = start = linkedList.returnHead()
    if n < k:
        return head
    start_head = None
    currNode = head
    prevGroupNode = None
    for i in range(n // k):
        count = 1
        prevNode = None
        while count <= k:
            next_node = currNode.next
            currNode.next = prevNode

            prevNode = currNode
            currNode = next_node
            count += 1
        if start_head is None:
            start_head = prevNode
        if prevGroupNode:
            prevGroupNode.next = prevNode
        prevGroupNode = start
        start = currNode
    if currNode:
        prevGroupNode.next = currNode
    return start_head if start_head else currNode








if __name__ == "__main__":
    linkedList1 = LinkedList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    k1 = 4
    # head = reverseNodesInKGroups(linkedList1, k1)
    # LinkedList(start_head=head).print_elements()

    linkedList2 = LinkedList([1, 2, 3])
    k2 = 4
    head = reverseNodesInKGroups(linkedList2, k2)
    LinkedList(start_head=head).print_elements()
    # LinkedList(star).print_elements()