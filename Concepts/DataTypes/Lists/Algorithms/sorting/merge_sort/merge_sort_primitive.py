def merge_two_sorted_arrays(arr1, arr2, arr):
    n = len(arr1)
    m = len(arr2)
    i = j = k = 0

    while i < n and j < m:
        if arr1[i] < arr2[j]:
            arr[k] = arr1[i]
            i += 1
        else:
            arr[k] = arr2[j]
            j += 1
        k += 1

    while i < n:
        arr[k] = arr1[i]
        i += 1
        k += 1

    while j < m:
        arr[k] = arr2[j]
        j += 1
        k += 1


def merge_sort(arr):
    if len(arr) == 1:
        return
    m = len(arr) // 2

    left = arr[:m]
    right = arr[m:]

    merge_sort(left)
    merge_sort(right)
    merge_two_sorted_arrays(left, right, arr)


if __name__ == '__main__':
    input_arr = [2, 1, 4, 3, 5, 6]
    merge_sort(input_arr)
    print(input_arr)
