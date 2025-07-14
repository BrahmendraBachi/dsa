
from Concepts.DataTypes.Lists.Algorithms.sorting.test_cases import test_cases

from Concepts.DataTypes.Lists.Algorithms.sorting.sorting_helpers import is_sorted


def selection_sort(arr):

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
    return arr


def main():
    try:
        for test_case in test_cases:
            copied_test_case = test_case["inp_arr"]
            selection_sort(copied_test_case)
            if not is_sorted(copied_test_case.copy()):
                raise Exception(f"input_arr: {test_case} \n",
                                f"Expected to be sorted, got this output: {copied_test_case}")
        print("Passed all testCases")

    except Exception as err:
        print(err)

if __name__ == '__main__':
    main()
