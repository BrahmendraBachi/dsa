from typing import List


def maxProfit(prices: List[int]) -> int:
    n = len(prices)
    dp = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(n)]

    def buy_or_sell(ind, buy, rem):
        if ind == n or rem == 0:
            return 0

        if dp[ind][buy][rem] != -1:
            return dp[ind][buy][rem]

        if not buy:
            profit = max(buy_or_sell(ind + 1, buy, rem), -prices[ind] + buy_or_sell(ind + 1, 1, rem))
        else:
            profit = max(buy_or_sell(ind + 1, buy, rem), prices[ind] + buy_or_sell(ind + 1, 0, rem - 1))

        dp[ind][buy][rem] = profit

        return profit

    return buy_or_sell(0, 0, 2)
