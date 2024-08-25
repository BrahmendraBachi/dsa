from concepts.linkedlist.linkedlist import LinkedList
from concepts.linkedlist.linkedListUtils import merge_sorted_linked_lists


def mergeSortedLinkedLists(linkedLists):
    if len(linkedLists) == 1:
        return linkedLists
    if len(linkedLists) == 0:
        return None
    m = len(linkedLists) // 2
    linkedList1 = mergeSortedLinkedLists(linkedLists[:m])
    linkedList2 = mergeSortedLinkedLists(linkedLists[m:])
    return merge_sorted_linked_lists(linkedList1, linkedList2)

    pass


def convertListsToLinkedLists(lists):
    return [LinkedList(_list) for _list in lists]


if __name__ == "__main__":
    lists_1 = [[1, 4, 5], [1, 3, 4], [2, 6]]

    linkedLists = convertListsToLinkedLists(lists_1)
    # for linkedList in linkedLists:
    #     linkedList.print_elements()


