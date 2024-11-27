def majorityElement(self, nums: List[int]) -> int:
    nums_dict = {}
    for num in nums:
        if num in nums_dict:
            nums_dict[num] += 1
            if nums_dict[num] > (len(nums) / 2):
                return num
        else:
            nums_dict[num] = 1
    return num
