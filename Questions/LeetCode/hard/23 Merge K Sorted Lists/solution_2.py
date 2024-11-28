from Concepts.linkedlist.linkedListUtils import convertListsToLinkedLists
from Concepts.linkedlist.linkedlist import LinkedList, Node
import heapq


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
    start_heads = [linkedList.returnHead() for linkedList in linkedLists_1]
    a = mergeKLists(start_heads)
    LinkedList(start_head=a).print_elements()
