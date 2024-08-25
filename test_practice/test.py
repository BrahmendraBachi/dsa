from concepts.linkedlist.linkedlist import LinkedList, Node
from concepts.linkedlist.linkedListUtils import merge_sorted_linked_lists, convertListsToLinkedLists
import heapq


def mergeSortedLinkedLists(linkedLists):
    if len(linkedLists) == 1:
        return linkedLists[0]
    if len(linkedLists) == 0:
        return None
    m = len(linkedLists) // 2
    linkedList1 = mergeSortedLinkedLists(linkedLists[:m])
    linkedList2 = mergeSortedLinkedLists(linkedLists[m:])
    return merge_sorted_linked_lists(linkedList1, linkedList2)


def mergeKLists(lists):
    heap = []
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, (node.val, i, node))

    D = Node()
    cur = D

    # n log k
    while heap:
        val, i, node = heapq.heappop(heap)
        cur.next = node
        cur = node
        node = node.next
        if node:
            heapq.heappush(heap, (node.val, i, node))

    return D.next


if __name__ == "__main__":
    lists_1 = [[1, 4, 5], [1, 3, 4], [2, 6]]

    linkedLists_1 = convertListsToLinkedLists(lists_1)
    mergeSortedLinkedLists(linkedLists_1).print_elements()

    # start_heads = [linkedList.returnHead() for linkedList in linkedLists_1]
    # a = mergeKLists(start_heads)
    # LinkedList(start_head=a).print_elements()
