from Concepts.DataTypes.Lists.Algorithms.sorting.sorting_helpers import is_sorted
from Concepts.DataTypes.Lists.Algorithms.sorting.test_cases import test_cases


def merge_two_sorted_arrays(arr1, arr2, arr):
    i = j = k = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr[k] = arr1[i]
            i += 1
        else:
            arr[k] = arr2[j]
            j += 1
        k += 1

    while i < len(arr1):
        arr[k] = arr1[i]
        i += 1
        k += 1

    while j < len(arr2):
        arr[k] = arr2[j]
        j += 1
        k += 1




def merge_sort(arr):
    if len(arr) <= 1:
        return

    m = len(arr) // 2

    left = arr[:m]
    right = arr[m:]

    merge_sort(left)
    merge_sort(right)

    merge_two_sorted_arrays(left, right, arr)


def run_test_case(inp, out):
    _inp = inp.copy()
    merge_sort(inp)

    try:
        for i in range(len(inp)):
            assert inp[i] == out[i]
            pass
        print("Test Passed!")
    except AssertionError:
        RED = '\033[31m'
        RESET = '\033[0m'
        print(
            RED + f"Test Failed! Input: {RESET} {_inp} {RED}, Expected: {RESET}{out}{RED}, Got: {RESET}{inp}"
        )

    except Exception as e:
        RED = '\033[31m'
        RESET = '\033[0m'
        print(RED + f"An unexpected error occurred: {e}" + RESET)


def main():
    try:
        for test_case in test_cases:
            test_case = test_case["inp_arr"]
            copied_test_case = test_case.copy()
            merge_sort(copied_test_case)
            if not is_sorted(copied_test_case):
                raise Exception(f"input_arr: {test_case['inp_arr']} \n",
                                f"Expected to be sorted, got this output: {copied_test_case}")
        print("Passed all testCases")

    except Exception as err:
        print(err)

if __name__ == "__main__":
    main()