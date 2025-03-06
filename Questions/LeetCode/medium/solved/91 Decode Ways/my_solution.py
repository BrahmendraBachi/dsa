def numDecodings(s: str) -> int:
    n = len(s)
    dp = {}

    def decode(i):
        if i in dp:
            return dp[i]
        if i > n:
            return 0
        if i == n:
            return 1
        if s[i] == '0':
            return 0

        way2 = 0
        if (i + 1) < n and int(s[i: i + 2]) <= 26:
            way2 = decode(i + 2)

        dp[i] = decode(i + 1) + way2
        return dp[i]

    return decode(0)
