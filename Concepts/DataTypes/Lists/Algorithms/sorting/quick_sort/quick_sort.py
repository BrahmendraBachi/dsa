def partition(arr):
    pivot = len(arr) - 1
    i, j = -1, 0
    while j < pivot:
        if arr[j] < arr[pivot]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        j += 1

    arr[i + 1], arr[pivot] = arr[pivot], arr[i + 1]

    return i + 1


def quick_sort(arr):quickarr) == 1:
        return arr
    par_ind = partition(arr)

    partition_ele = arr[par_ind]
    left_arr = quick_sort(arr[:par_ind])
    right_arr = quick_sort(arr[par_ind + 1:])

    return left_arr + [partition_ele] + right_arr


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
    test_cases = [
        {"input": [], "output": []},
        {"input": [5], "output": [5]},
        {"input": [1, 2, 3, 4, 5], "output": [1, 2, 3, 4, 5]},
        {"input": [5, 4, 3, 2, 1], "output": [1, 2, 3, 4, 5]},
        {"input": [1, 3, 5, 2, 3, 1], "output": [1, 1, 2, 3, 3, 5]},
        {"input": [2, 2, 2, 2, 2], "output": [2, 2, 2, 2, 2]},
        {"input": [-5, 2, -1, 0, 3], "output": [-5, -1, 0, 2, 3]},
        {"input": [0, -3, 5, -1, 2], "output": [-3, -1, 0, 2, 5]},
        {"input": [1, 2, 3, 5, 4], "output": [1, 2, 3, 4, 5]}
    ]

    for test_case in test_cases:
        run_test_case(test_case["input"], test_case["output"])


if __name__ == "__main__":
    main()
