from Concepts.DataTypes.Heap.max_heap_from_array import Max_Heap


def heap_sort(arr):
    max_heap = Max_Heap(arr)
    max_heap.sort()


if __name__ == "__main__":
    input_arr = [9, 4, 8, 3, 1, 6, 5, 2]
    heap_sort(input_arr)
    print(input_arr)
