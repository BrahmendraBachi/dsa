from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    diff = {}
    n = len(nums)
    for i in range(n):
        if target - nums[i] in diff:
            return [diff[target - nums[i]], i]
        diff[nums[i]] = i
