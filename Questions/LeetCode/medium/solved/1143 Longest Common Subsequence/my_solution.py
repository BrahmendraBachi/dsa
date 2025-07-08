def longestCommonSubsequence(text1: str, text2: str) -> int:
    n, m = len(text1), len(text2)
    dp = [[-1 for _ in range(m + 1)] for _ in range(n + 1)]
    for ind in range(m + 1):
        dp[n][ind] = 0
    for ind in range(n + 1):
        dp[ind][m] = 0

    def getLongest(i, j) -> int:
        if dp[i][j] != -1:
            return dp[i][j]
        if i >= len(text1) or j >= len(text2):
            dp[i][j] = 0
        elif text1[i] == text2[j]:
            dp[i][j] = 1 + getLongest(i + 1, j + 1)
        else:
            dp[i][j] = max(getLongest(i + 1, j), getLongest(i, j + 1))

        return dp[i][j]

    longest = getLongest(0, 0)
    return longest
