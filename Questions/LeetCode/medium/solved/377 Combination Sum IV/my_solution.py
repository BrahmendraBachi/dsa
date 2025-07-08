from typing import List


def combinationSum4(nums: List[int], target: int) -> int:
    n = len(nums)

    dp = [-1] * (target + 1)

    def combinationSum(rem_tar):
        if rem_tar < 0:
            return 0
        if dp[rem_tar] != -1:
            return dp[rem_tar]
        if rem_tar == 0:
            return 1
        total_count = 0
        for i in range(n):
            total_count += combinationSum(rem_tar - nums[i])
        dp[rem_tar] = total_count
        return dp[rem_tar]

    return combinationSum(target)
