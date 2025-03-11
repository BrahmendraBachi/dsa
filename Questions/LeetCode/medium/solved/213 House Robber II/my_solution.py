from typing import List


def rob(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]

    if len(nums) == 2:
        return max(nums[0], nums[1])

    def helper(arr):
        dp1, dp2 = arr[0], max(arr[0], arr[1])
        for i in range(2, len(arr)):
            temp = max(dp2, dp1 + arr[i])
            dp1 = dp2
            dp2 = temp

        return dp2

    return max(helper(nums[1:]), helper(nums[:-1]))