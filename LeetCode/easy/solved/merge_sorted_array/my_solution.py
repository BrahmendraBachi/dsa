def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    sorted_arr = [0] * (m + n)
    ptr1, ptr2 = 0, 0
    while ptr1 + ptr2 < m + n:
        if ptr1 < m and ptr2 < n:
            if nums1[ptr1] < nums2[ptr2]:
                sorted_arr[ptr1 + ptr2] = nums1[ptr1]
                ptr1 += 1
            else:
                sorted_arr[ptr1 + ptr2] = nums2[ptr2]
                ptr2 += 1
            continue
        if ptr1 >= m:
            sorted_arr[ptr1 + ptr2] = nums2[ptr2]
            ptr2 += 1
            continue
        if ptr2 >= n:
            sorted_arr[ptr1 + ptr2] = nums1[ptr1]
            ptr1 += 1
            continue
        break
    print(sorted_arr)
    for i in range(len(sorted_arr)):
        nums1[i] = sorted_arr[i]
