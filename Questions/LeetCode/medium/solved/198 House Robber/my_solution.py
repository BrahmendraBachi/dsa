from typing import List


def rob(nums: List[int]) -> int:
    dp = {}
    n = len(nums)

    def find_max_rob(curr_rob):
        if curr_rob in dp:
            return dp[curr_rob]

        max_rob = nums[curr_rob]
        next_max_robbery = 0
        for next_rob in range(curr_rob + 2, n):
            next_robbery = find_max_rob(next_rob)
            next_max_robbery = max(next_max_robbery, next_robbery)

        max_rob += next_max_robbery
        dp[curr_rob] = max_rob
        return dp[curr_rob]

    max_robbery = 0
    for i in range(n):
        max_robbery = max(find_max_rob(i), max_robbery)

    return max_robbery
