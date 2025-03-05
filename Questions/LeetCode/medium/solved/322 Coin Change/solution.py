from typing import List


def coinChange(coins: List[int], amount: int) -> int:
    dp = {}

    def find_min(curr_amount):
        if curr_amount in dp:
            return dp[curr_amount]
        if curr_amount == 0:
            return 0
        if curr_amount < 0:
            return float('inf')

        min_count = float('inf')
        for coin in coins:
            res = find_min(curr_amount - coin)
            if res != float('inf'):
                min_count = min(min_count, res + 1)
        dp[curr_amount] = min_count
        return min_count

    result = find_min(amount)
    return result if result != float('inf') else -1
