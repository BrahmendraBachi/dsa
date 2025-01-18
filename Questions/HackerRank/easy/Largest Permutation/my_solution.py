def largestPermutation(k, arr):
    n = len(arr)
    sorted_arr = arr.copy()
    sorted_arr.sort()
    arr_dict = {}
    for ind, ele in enumerate(arr):
        arr_dict[ele] = ind
    curr_ind = 0
    while len(sorted_arr) and k > 0 and curr_ind < n:
        top_ele = sorted_arr.pop()
        ele_ind = arr_dict[top_ele]
        if ele_ind != curr_ind:
            arr_dict[arr[curr_ind]] = ele_ind
            arr[curr_ind], arr[ele_ind] = arr[ele_ind], arr[curr_ind]
            del arr_dict[top_ele]
            k -= 1
        curr_ind += 1
    return arr