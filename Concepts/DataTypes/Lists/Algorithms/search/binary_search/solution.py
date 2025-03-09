def binary_search(arr, target, l=0, r=None):
    if r is None:
        r = len(arr) - 1
    if l > r:
        return -1

    m = (l + r) // 2
    if arr[m] == target:
        return m

    if arr[m] < target:
        return binary_search(arr, target, m + 1, r)
    else:
        return binary_search(arr, target, l, m - 1)


def main():
    test_cases = [
        {"input": ([], 5), "output": -1},  # Empty array
        {"input": ([5], 5), "output": 0},  # Single element, found
        {"input": ([5], 3), "output": -1},  # Single element, not found
        {"input": ([1, 2, 3, 4, 5], 1), "output": 0},  # Target at beginning
        {"input": ([1, 2, 3, 4, 5], 5), "output": 4},  # Target at end
        {"input": ([1, 2, 3, 4, 5], 3), "output": 2},  # Target in middle
        {"input": ([1, 2, 3, 4, 5], 0), "output": -1},  # Target smaller than smallest
        {"input": ([1, 2, 3, 4, 5], 6), "output": -1},  # Target larger than largest
        {"input": ([1, 3, 5, 7, 9], 4), "output": -1},  # Target in between
        {"input": ([-5, -2, 0, 3, 7], 0), "output": 2},  # Negative numbers, found
        {"input": ([-5, -2, 0, 3, 7], -2), "output": 1},  # Negative numbers, found
        {"input": ([2, 2, 2, 2, 2], 3), "output": -1},  # all same elements, target not found
    ]
    for test_case in test_cases:
        inp, target, out = test_case["input"][0], test_case["input"][1], test_case["output"]
        result = binary_search(inp, target)
        try:
            assert result == out
            print("Test Passed!")
        except AssertionError:
            RED = '\033[31m'
            RESET = '\033[0m'
            print(RED + f"Test Failed! Input: {RESET} {inp} {RED}, target:{RESET} {target} {RED}, Expected: {RESET}{out}{RED}, Got: {RESET}{result}")

        except Exception as e:
            RED = '\033[31m'
            RESET = '\033[0m'
            print(RED + f"An unexpected error occurred: {e}" + RESET)


if __name__ == "__main__":
    arr1 = [5, 25, 75]
    main()
