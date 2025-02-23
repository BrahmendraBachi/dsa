from typing import List


def majorityElement(self, nums: List[int]) -> int:
    nums_dict = {}
    num = 0
    for num in nums:
        if num in nums_dict:
            nums_dict[num] += 1
            if nums_dict[num] > (len(nums) / 2):
                return num
        else:
            nums_dict[num] = 1
    return num
