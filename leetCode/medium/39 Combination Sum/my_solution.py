def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
    candidates.sort()
    all_combs = []
    comb = []

    def isValidComb(curr_sum, i):
        nonlocal comb
        if curr_sum == target:
            all_combs.append(comb.copy())
            return True
        if curr_sum + candidates[i] <= target:
            for j in range(i, len(candidates)):
                comb.append(candidates[j])
                isValid = isValidComb(curr_sum + candidates[j], j)
                comb.pop()
                if isValid:
                    break
        return

    isValidComb(0, 0)
    return all_combs


# Second Solution
def combinationSum_1(self, candidates: List[int], target: int) -> List[List[int]]:
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
            return
        isValidComb(0, 0)
        return all_combs