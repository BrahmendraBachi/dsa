def maxMin(k, arr):
    # Write your code here
    arr.sort()
    min_value = None
    n = len(arr)
    if k == n == 2:
        return arr[1] - arr[0]
    for i in range(n - k + 1):
        curr_min = arr[i + k - 1] - arr[i]
        if min_value is None or curr_min < min_value:
            min_value = curr_min
    return 0 if min_value is None else min_value
