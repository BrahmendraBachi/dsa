def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


if __name__ == "__main__":
    input_arr = [4, 9, 1, 3, 5, 2]
    insertion_sort(input_arr)
    print(input_arr)
