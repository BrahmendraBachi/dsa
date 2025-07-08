from typing import List


def coinChange(coins: List[int], amount: int) -> int:
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    print(dp)
    return dp[amount] if dp[amount] != float('inf') else -1


def main():
    coins = [2, 5]
    amount = 11
    print(coinChange(coins, amount))


if __name__ == "__main__":
    main()