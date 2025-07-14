from Concepts.DataTypes.Lists.Algorithms.sorting.sorting_helpers import is_sorted
from Concepts.DataTypes.Lists.Algorithms.sorting.test_cases import test_cases

def merge_two_sorted_lists(arr1, arr2):
    new_arr = []
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            new_arr.append(arr1[i])
            i += 1
        else:
            new_arr.append(arr2[j])
            j += 1

    if i < len(arr1):
        return new_arr + arr1[i:]

    if j < len(arr2):
        return new_arr + arr2[j:]

    return new_arr

def merge_sort(arr):

    if len(arr) == 0 or len(arr) == 1:
        return arr

    m = len(arr) // 2
    left_sorted_array = merge_sort(arr[:m])
    right_sorted_array = merge_sort(arr[m:])

    return merge_two_sorted_lists(left_sorted_array, right_sorted_array)


def main():
    try:
        for test_case in test_cases:
            copied_test_case = test_case["inp_arr"]
            sorted_array = merge_sort(copied_test_case)
            if not is_sorted(sorted_array):
                raise Exception(f"input_arr: {test_case['inp_arr']} \n",
                                f"Expected to be sorted, got this output: {copied_test_case}")
        print("Passed all testCases")

    except Exception as err:
        print(err)

if __name__ == "__main__":
    main()
