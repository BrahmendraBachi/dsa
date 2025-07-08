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

    if j < len(arr2):
        return new_arr + arr2[j:]
    if i < len(arr1):
        return new_arr + arr1[i:]
    return new_arr


def merge_sort(arr):
    if len(arr) == 1 or len(arr) == 0:
        return arr

    m = len(arr) // 2
    left = merge_sort(arr[:m])
    right = merge_sort(arr[m:])

    return merge_two_sorted_lists(left, right)


def run_test_case(inp, out):
    res = merge_sort(inp)

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
