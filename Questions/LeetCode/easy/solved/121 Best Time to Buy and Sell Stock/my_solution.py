from typing import List


def maxProfit(prices: List[int]) -> int:
    n = len(prices)
    min_prices_dp, max_prices_dp = [0] * len(prices), [0] * len(prices)
    min_prices_dp[0] = prices[0]
    max_prices_dp[-1] = prices[-1]
    for i in range(1, n):
        min_prices_dp[i] = min(prices[i], min_prices_dp[i - 1])
        max_prices_dp[n - i - 1] = max(max_prices_dp[n - i], prices[n - i - 1])

    max_profit = 0
    print(max_prices_dp)
    print(min_prices_dp)
    for i in range(n):
        max_profit = max(max_profit, max_prices_dp[i] - min_prices_dp[i])

    return max_profit
