def bubble_sort(arr):
    n = len(arr)
    for i in range(len(arr)):
        is_swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_swapped = True
        if not is_swapped:
            break


if __name__ == "__main__":
    input1 = [3, 2, 4, 2, 0, 9]
    bubble_sort(input1)
    print(input1)
