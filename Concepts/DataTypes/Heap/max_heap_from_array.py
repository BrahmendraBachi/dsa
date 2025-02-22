# [9, 4, 8, 3, 1, 6, 5, 2]
def heapify(arr, i, n):
    largest = i
    left, right = (2 * i) + 1, (2 * i) + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[largest], arr[i] = arr[i], arr[largest]
        heapify(arr, largest, n)


def convert_into_heap(arr):
    n = len(arr)
    for i in range((n // 2) - 1, -1, -1):
        heapify(arr, i, n)


if __name__ == "__main__":
    input_arr = [5, 3, 8, 4, 1, 6, 9, 2]
    convert_into_heap(input_arr)
    print(input_arr)