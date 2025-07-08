from typing import List


def coinChange(self, coins: List[int], amount: int) -> int:
    dp = {}

    def find_min(curr_amount=0, n_coins=0):
        if curr_amount in dp:
            return None if dp[curr_amount] == -1 else dp[curr_amount] + n_coins
        if curr_amount > amount:
            return None
        if curr_amount == amount:
            return n_coins

        min_count = None
        for coin in coins:
            curr_count = find_min(curr_amount + coin, n_coins + 1)
            if curr_count is None:
                continue
            if min_count is None or min_count > curr_count:
                min_count = curr_count
        dp[curr_amount] = -1 if min_count is None else min_count - n_coins
        return min_count

    res = find_min()
    return -1 if res is None else res
