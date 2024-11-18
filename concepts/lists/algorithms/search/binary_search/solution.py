def binary_search(arr, target, l=0, r=None):
    n = len(arr)
    if r is None:
        r = n - 1
    m = (l + r) // 2
    if l > r:
        return -1
    if arr[m] == target:
        return m
    if arr[m] < target:
        return binary_search(arr, target, m + 1, r)
    return binary_search(arr, target, l, m - 1)


if __name__ == "__main__":
    arr1 = [5, 25, 75]
    print()

