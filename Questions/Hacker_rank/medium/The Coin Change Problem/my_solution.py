def getWays(n, c):
    # Write your code here
    c.sort()
    return recursive_count(n, c)


def recursive_count(n, c, start=0, dp=None):
    # Write your code here
    if dp is None:
        dp = {}
    hashKey = str(n) + " " + str(start)
    if hashKey in dp:
        return dp[hashKey]
    if n == 0:
        return 1
    count = 0
    for i in range(start, len(c)):
        if n - c[i] >= 0:
            count += recursive_count(n - c[i], c, i)
            continue
        break
    dp[hashKey] = count
    return count