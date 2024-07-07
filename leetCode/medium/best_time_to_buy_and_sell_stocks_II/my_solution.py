def maxProfit(self, prices: List[int]) -> int:
    n = len(prices)
    prices_new = [0] * n
    prices_new[0] = prices[0]
    curr = prices[0]
    i = 1
    for j in range(1, n):
        if curr == prices[j]:
            continue
        curr = prices[j]
        prices_new[i] = curr
        i += 1
    prices = prices_new[:i]

    n = i

    if n == 1:
        return 0
    mins = []
    maxs = []

    for i in range(n):
        if i == 0 or i == n - 1:
            if i == 0 and prices[i + 1] > prices[i]:
                mins.append(prices[i])
            if i == n - 1 and prices[i] > prices[i - 1]:
                maxs.append(prices[i])
            continue
        if prices[i - 1] > prices[i] and prices[i + 1] > prices[i]:
            mins.append(prices[i])
        if prices[i - 1] < prices[i] and prices[i + 1] < prices[i]:
            maxs.append(prices[i])
    return sum(maxs) - sum(mins)



