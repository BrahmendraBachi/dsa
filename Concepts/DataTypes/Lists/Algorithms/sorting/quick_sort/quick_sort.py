def partition(arr):
    pivot = len(arr) - 1
    i = -1
    for j in range(0, pivot):
        if arr[j] < arr[pivot]:
            i += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[i + 1], arr[pivot] = arr[pivot], arr[i + 1]
    return i + 1


def quick_sort(arr):
    if len(arr) == 1:
        return arr
    pivot = partition(arr)

    left = quick_sort(arr[:pivot]) if pivot > 0 else []
    right = quick_sort(arr[pivot + 1:]) if pivot + 1 < len(arr) else []
    return left + [arr[pivot]] + right


if __name__ == "__main__":
    input1 = [9, 6, 5, 3, 1, 4]
    input1 = quick_sort(input1)
    print(input1)
