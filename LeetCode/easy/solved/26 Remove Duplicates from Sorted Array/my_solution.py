def removeDuplicates(nums):
    if len(nums) == 0:
        return 0
    prev = nums[0]
    ptr1 = 1
    for ptr2 in range(1, len(nums)):
        if prev == nums[ptr2]:
            continue
        nums[ptr1] = nums[ptr2]
        prev = nums[ptr2]
        ptr1 += 1
    return ptr1
