from typing import List


def largestNumber(nums: List[int]) -> str:
    if nums.count(0) == len(nums):
        return '0'

    def merge_sorted_arrays(arr1, arr2):
        new_arr = []

        ptr1, ptr2 = 0, 0
        while ptr1 < len(arr1) and ptr2 < len(arr2):
            comb1 = int(arr1[ptr1] + arr2[ptr2])
            comb2 = int(arr2[ptr2] + arr1[ptr1])
            # print(comb1, comb2)
            if comb2 > comb1:
                new_arr.append(arr2[ptr2])
                ptr2 += 1
            else:
                new_arr.append(arr1[ptr1])
                ptr1 += 1
        # print(arr1, arr2, ptr1, ptr2, new_arr)
        while ptr1 < len(arr1):
            new_arr.append(arr1[ptr1])
            ptr1 += 1

        while ptr2 < len(arr2):
            new_arr.append(arr2[ptr2])
            ptr2 += 1
        return new_arr

    def sort_array(arr):
        if len(arr) == 1 or len(arr) == 0:
            return arr
        m = len(arr) // 2

        arr1 = sort_array(arr[:m])
        arr2 = sort_array(arr[m:])

        return merge_sorted_arrays(arr1, arr2)

    nums = [str(i) for i in nums]

    nums = sort_array(nums)

    return "".join(nums)