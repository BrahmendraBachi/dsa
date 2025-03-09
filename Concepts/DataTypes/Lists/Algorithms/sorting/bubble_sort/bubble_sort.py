def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        is_swapped = False
        for j in range(0, n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                is_swapped = True

        if not is_swapped:
            break


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
        inp, out = test_case["input"], test_case["output"]
        _inp = inp.copy()
        bubble_sort(inp)

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


if __name__ == "__main__":
    main()
