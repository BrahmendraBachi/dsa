from dsa.Concepts.DataTypes.Lists.Algorithms.sorting.test_cases import test_cases


def is_sorted(arr):

    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            return False
    return True

def bubble_sort(arr):
    n = len(arr)

    is_swapped = False
    for i in range(n):
        for j in range(1, n):
            if arr[i - 1] > arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                is_swapped = True

        if not is_swapped:
            break

def main():
    try:
        for test_case in test_cases:
            copied_test_case = test_case
            bubble_sort(copied_test_case)
            if not is_sorted(copied_test_case.copy()):
                raise Exception(f"input_arr: {test_case} \n",
                                f"Expected to be sorted, got this output: {copied_test_case}")
        print("Passed all testCases")

    except Exception as err:
        print(err)

if __name__ == "__main__":
    main()