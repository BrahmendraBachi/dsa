def majorityElement(nums):
    prev, count = nums[0], 1
    for num in nums[1:]:
        if num != prev:
            count -= 1
        else:
            count += 1
        if count == 0:
            prev = num
            count = 1
    return prev
