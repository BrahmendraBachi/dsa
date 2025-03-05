from typing import List


def rob(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    rob1 = nums[0]
    rob2 = max(nums[0], nums[1])
    n = len(nums)
    for i in range(2, n):
        temp = max(rob1 + nums[i], rob2)
        rob1 = rob2
        rob2 = temp

    return rob2