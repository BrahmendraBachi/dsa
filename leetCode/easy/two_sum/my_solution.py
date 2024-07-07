def two_sum(self, nums: List[int], target: int) -> List[int]:
    diff = {}
    n = len(nums)
    for i in range(n):
        if target - nums[i] in diff:
            return [diff[target - nums[i]], i]
        diff[nums[i]] = i


