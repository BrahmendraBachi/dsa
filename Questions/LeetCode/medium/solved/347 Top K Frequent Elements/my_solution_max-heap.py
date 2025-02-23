def topKFrequent(self, nums, k):
    nums_count = {}
    for num in nums:
        if num in nums_count:
            nums_count[num] += 1
        else:
            nums_count[num] = 1

    items_count = [item for item in nums_count.items()]
    n = len(items_count)
    for i in range(n // 2 - 1, -1, -1):
        self.heapify(items_count, i)
    max_count = []
    for i in range(k):
        item = self.heap_pop(items_count)
        max_count.append(item[0])
    return max_count


def heapify(self, items, ind):
    left = 2 * ind + 1
    right = 2 * ind + 2
    largest = ind

    if left < len(items) and items[left][1] > items[largest][1]:
        largest = left
    if right < len(items) and items[right][1] > items[largest][1]:
        largest = right
    if largest != ind:
        items[largest], items[ind] = items[ind], items[largest]
        self.heapify(items, largest)


def heap_pop(self, items):
    n = len(items)
    items[n - 1], items[0] = items[0], items[n - 1]
    item = items.pop()
    self.heapify(items, 0)
    return item
