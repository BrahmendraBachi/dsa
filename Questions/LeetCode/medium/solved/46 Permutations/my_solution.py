from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    res = []

    def permutate_all(ind):
        if ind == len(nums):
            res.append(nums.copy())
            return

        for i in range(ind, len(nums)):
            nums[ind], nums[i] = nums[i], nums[ind]
            permutate_all(ind + 1)
            nums[ind], nums[i] = nums[i], nums[ind]

    permutate_all(0)
    return res
