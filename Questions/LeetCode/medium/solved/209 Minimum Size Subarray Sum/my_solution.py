from typing import List


def minSubArrayLen(target: int, nums: List[int]) -> int:
    len_n = len(nums)
    l, r = 0, 1
    if len(nums) == 1:
        return 0 if nums[0] < target else 1
    min_len = None
    if nums[l] >= target or nums[r] >= target:
        return 1
    slide_sum = nums[0] + nums[1]
    while l <= r < len_n:
        if slide_sum >= target:
            min_len = min(min_len, r - l + 1) if min_len is not None else r - l + 1
            slide_sum -= nums[l]
            l = l + 1
            if nums[l] >= target:
                return 1
        else:
            r = r + 1
            if r >= len_n:
                break
            if nums[r] >= target:
                return 1
            slide_sum += nums[r]
    return 0 if min_len is None else min_len
