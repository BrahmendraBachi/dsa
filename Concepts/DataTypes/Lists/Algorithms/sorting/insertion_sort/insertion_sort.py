from Concepts.DataTypes.Lists.Algorithms.sorting.sorting_helpers import is_sorted
from Concepts.DataTypes.Lists.Algorithms.sorting.test_cases import test_cases

def insertion_sort(arr):

    for i in range(1, len(arr)):
        j = 0
        temp = arr[i]
        while j < i:
            if arr[j] > temp:
                temp, arr[j] = arr[j], temp
            j += 1

        arr[i] = temp


def main():
    try:
        for test_case in test_cases:
            copied_test_case = test_case["inp_arr"]
            insertion_sort(copied_test_case)
            if not is_sorted(copied_test_case.copy()):
                raise Exception(f"input_arr: {test_case['inp_arr']} \n",
                                f"Expected to be sorted, got this output: {copied_test_case}")
        print("Passed all testCases")

    except Exception as err:
        print(err)


if __name__ == "__main__":
    main()