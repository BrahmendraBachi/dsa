from functools import cmp_to_key
from typing import List


def largestNumber(nums: List[int]) -> str:
    if nums.count(0) == len(nums):
        return '0'

    nums = [str(nums[i]) for i in range(len(nums))]

    def compare(n1, n2):
        if n1 + n2 > n2 + n1:
            return -1
        else:
            return 1

    nums = sorted(nums, key=cmp_to_key(compare))

    return "".join(nums)
