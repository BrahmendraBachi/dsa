from concepts.linkedlist.linkedlist import LinkedList
from concepts.linkedlist.linkedListUtils import merge_sorted_linked_lists, convertListsToLinkedLists


def mergeSortedLinkedLists(linkedLists):
    if len(linkedLists) == 1:
        return linkedLists[0]
    if len(linkedLists) == 0:
        return None
    m = len(linkedLists) // 2
    linkedList1 = mergeSortedLinkedLists(linkedLists[:m])
    linkedList2 = mergeSortedLinkedLists(linkedLists[m:])
    return merge_sorted_linked_lists(linkedList1, linkedList2)


if __name__ == "__main__":
    lists_1 = [[1, 4, 5], [1, 3, 4], [2, 6]]

    linkedLists_1 = convertListsToLinkedLists(lists_1)
    mergeSortedLinkedLists(linkedLists_1).print_elements()
