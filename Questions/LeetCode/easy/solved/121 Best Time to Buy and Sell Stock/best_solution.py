from typing import List


def maxProfit(prices: List[int]) -> int:
    mini = maxi = prices[0]
    profit = 0
    for price in prices[1:]:
        if price < mini:
            mini = maxi = price
        elif price > maxi:
            maxi = price
            profit = max(profit, maxi - mini)
    return profit
