def combinations(nums, start=0, comb=None):
    if comb is None:
        comb = []
    combs = []
    if start == len(nums):
        return combs
    for i in range(start, len(nums)):
        comb.append(nums[i])
        combs.append(comb.copy())
        combs += combinations(nums, i + 1, comb)
        comb.pop()
    return combs


if __name__ == "__main__":
    print(combinations(list(range(1, 18))))
