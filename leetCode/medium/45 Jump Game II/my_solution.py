def jump(self, nums):
    min_counts = [0] * len(nums)
    for start in range(len(nums) - 2, -1, -1):
        if nums[start] == 0:
            min_counts[start] = 1000000
            continue
        end = start + nums[start] + 1
        if end >= len(nums):
            min_counts[start] = 1
            continue
        min_counts[start] = 1 + min(min_counts[start + 1: end])
    return min_counts[0]