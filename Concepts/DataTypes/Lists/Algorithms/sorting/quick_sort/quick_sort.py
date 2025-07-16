from Concepts.DataTypes.Lists.Algorithms.sorting.insertion_sort.insertion_sort import insertion_sort
from Concepts.DataTypes.Lists.Algorithms.sorting.sorting_helpers import is_sorted
from Concepts.DataTypes.Lists.Algorithms.sorting.test_cases import test_cases


def partition(arr):
    # consider last element as our pivot
    i = -1
    j = 0
    pivot = len(arr) - 1

    while j < pivot:
        if arr[j] < arr[pivot]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        j += 1

    i += 1
    arr[i], arr[pivot] = arr[pivot], arr[i]

    return i


def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    p_ind = partition(arr)

    left_arr = arr[:p_ind]
    right_arr = arr[p_ind + 1:]

    arr = quick_sort(left_arr) + [arr[p_ind]] + quick_sort(right_arr)

    return arr

def run_test_case(inp, out):
    res = quick_sort(inp)

    try:
        for i in range(len(inp)):
            assert out[i] == res[i]
            pass
        print("Test Passed!")
    except AssertionError:
        RED = '\033[31m'
        RESET = '\033[0m'
        print(
            RED + f"Test Failed! Input: {RESET} {inp} {RED}, Expected: {RESET}{out}{RED}, Got: {RESET}{res}"
        )

    except Exception as e:
        RED = '\033[31m'
        RESET = '\033[0m'
        print(RED + f"An unexpected error occurred: {e}" + RESET)


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
