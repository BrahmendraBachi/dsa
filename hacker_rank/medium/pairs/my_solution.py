def pairs(k, arr):
    arr_dict = {}
    n = len(arr)
    count = 0
    for i in range(n):
        arr_dict[arr[i]] = i
    for i in range(n):
        target = k + arr[i]
        if target in arr_dict:
            count += 1
    return count


if __name__ == '__main__':
    pass