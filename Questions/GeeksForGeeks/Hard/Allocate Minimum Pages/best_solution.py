def check_for_fit(arr, k, max_p):
    count = 1
    curr_sum = 0
    for price in arr:
        if curr_sum + price > max_p:
            count += 1
            curr_sum = price
        else:
            curr_sum += price
    return count <= k


# Function to find minimum number of pages.
def findPages(arr, k):
    if len(arr) < k:
        return -1

    low = max(arr)
    high = sum(arr)
    res = -1

    while low <= high:
        mid = low + (high - low) // 2
        if check_for_fit(arr, k, mid):
            res = mid
            high = mid - 1
        else:
            low = mid + 1
    return res

if __name__ == "__main__":
    input1 = ([3, 1, 1], 2)
    input2 = ([3, 1, 2, 1, 6], 3)
    print(findPages(input2[0], input2[1]))
    # print(find_pages(list(range(1, 31)), 10))
    # input3 =

