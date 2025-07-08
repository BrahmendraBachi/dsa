from dsa.Concepts.DataTypes.Lists.Algorithms.search.binary_search.test_cases import test_cases


def binary_search(arr, target, l=0, r=None):
    if r is None:
        r = len(arr) - 1
    if l > r:
        return -1
    m = (l + r) // 2
    if arr[m] < target:
        return binary_search(arr, target, m + 1, r)
    elif arr[m] > target:
        return binary_search(arr, target, l, m - 1)
    else:
        return m


if __name__ == "__main__":
    try:

        for test_case in test_cases:
            act_out = binary_search(test_case["inp_arr"], test_case["tar_val"])
            if act_out != test_case["exp_out"]:
                raise Exception(
                    f"input_arr: {test_case['inp_arr']},\n"
                    f"exp_out: {test_case['exp_out']},\n"
                    f"actual output: {act_out}"
                )


        print("Passed all testCases")
    except Exception as err:
        print(err)


