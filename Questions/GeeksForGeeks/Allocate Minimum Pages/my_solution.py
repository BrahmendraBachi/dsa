def find_pages(arr, k):
    def allocate(rem_arr, rem_k, start=1, allocation_arr=None):
        end = len(rem_arr) - rem_k + 1
        if allocation_arr is None:
            allocation_arr = []
        if rem_k == 1:
            return [max(allocation_arr + [sum(rem_arr)])]
        allocations = []
        for i in range(1, end + 1):
            curr_sum = sum(rem_arr[:i])
            allocation_arr.append(curr_sum)
            allocations += allocate(rem_arr[i:], rem_k - 1, i, allocation_arr)
            allocation_arr.pop()
        return allocations
    all_allocations = allocate(arr, k)
    return min(all_allocations)

if __name__ == "__main__":
    input1 = ([3, 1, 1], 2)
    input2 = ([3, 1, 2, 1, 6], 3)
    print(find_pages(input2[0], input2[1]))
    # print(find_pages(list(range(1, 31)), 10))
    # input3 =
