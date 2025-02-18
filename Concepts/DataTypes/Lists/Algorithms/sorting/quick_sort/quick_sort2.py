def partition(arr, low, high):
    i = low - 1
    pivot = high
    for j in range(low, pivot):
        if arr[j] < arr[pivot]:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]

    arr[i + 1], arr[pivot] = arr[pivot], arr[i + 1]
    return i + 1


def quick_sort(arr, low=0, high=None):
    if high is None:
        high = len(arr) - 1
    if low >= high:
        return

    pivot = partition(arr, low, high)

    quick_sort(arr, low, pivot - 1)
    quick_sort(arr, pivot + 1, high)


if __name__ == "__main__":
    input1 = [9, 1, 3, 2, 6, 7, 4]
    quick_sort(input1)
    print(input1)
