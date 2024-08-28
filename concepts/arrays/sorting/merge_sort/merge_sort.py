def merge_two_sorted_lists(arr1, arr2):
    merged_arr = []
    i = j = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_arr.append(arr1[i])
            i += 1
        else:
            merged_arr.append(arr2[j])
            j += 1

    return merged_arr + arr2[j:] if i >= len(arr1) else merged_arr + arr1[i:]

def merge_sort(arr):
    if len(arr) == 1 or len(arr) == 0:
        return arr
    m = len(arr) // 2
    arr1 = merge_sort(arr[:m])
    arr2 = merge_sort(arr[m:])
    return merge_two_sorted_lists(arr1, arr2)


if __name__ == "__main__":

    input1 = [2, 3, 5, 4, 6, 1, 1, 1]
    sorted_input1 = merge_sort(input1)
    print(sorted_input1)
