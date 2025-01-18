def minimumAbsoluteDifference(arr):
    arr.sort()
    min_diff = None
    # print(arr)
    for i in range(1, len(arr)):
        diff = abs(arr[i] - arr[i-1])
        # print(diff, min_diff)
        if min_diff is None or diff < min_diff:
            min_diff = diff
    return min_diff