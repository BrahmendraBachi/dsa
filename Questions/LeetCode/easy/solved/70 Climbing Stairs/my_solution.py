def climbStairs(stairs: int) -> int:
    dp = {}

    def fibb(n):
        if n == 0 or n == 1:
            return 1
        if n in dp:
            return dp[n]
        dp[n] = fibb(n - 1) + fibb(n - 2)
        return dp[n]

    return fibb(stairs)