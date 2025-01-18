def minimumLoss(prices):
    n = len(prices)
    min_profit = None
    prices_ind_dict = {}
    for i, price in enumerate(prices):
        prices_ind_dict[price] = i
    prices.sort(reverse=True)

    for i in range(1, n):
        k = 0
        while True:
            if prices_ind_dict[prices[i + k]] > prices_ind_dict[prices[i + k - 1]]:
                diff = abs(prices[i + k] - prices[i + k - 1])
                if min_profit is None or min_profit > diff:
                    min_profit = diff
                break
            k += 1
            if i + k >= n:
                break
    return min_profit