def selection_sort(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


if __name__ == '__main__':
    print(selection_sort([2, 3, 4, 1, 2, 5]))
