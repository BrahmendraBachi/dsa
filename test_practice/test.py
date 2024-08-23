def getAllValidCombs(candidates, target):
    all_combs = []
    comb = []

    def isValidComb(curr_sum, i):
        nonlocal comb
        if curr_sum > target:
            return
        if curr_sum == target:
            all_combs.append(comb.copy())
            return
        for j in range(i, len(candidates)):
            comb.append(candidates[j])
            isValidComb(curr_sum + candidates[j], j)
            comb.pop()

    isValidComb(0, 0)
    return all_combs


if __name__ == "__main__":
    print(getAllValidCombs([2, 3, 6, 7], 7))
    print(getAllValidCombs([8, 7, 4, 3], 11))
    print(getAllValidCombs([2, 3, 5], 8))
    print(getAllValidCombs([2], 1))
    print(getAllValidCombs([2, 3, 5], 10))
    print(getAllValidCombs([5, 3, 2], 10))
