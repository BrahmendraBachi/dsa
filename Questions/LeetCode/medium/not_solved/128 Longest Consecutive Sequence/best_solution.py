def longestConsecutive(self, nums) -> int:
    if len(nums) == 0:
        return 0
    nums = set(nums)
    count = max_count = 1
    for num in nums:
        if num + 1 not in nums:
            while (num - 1) in nums:
                count += 1
                num -= 1
            max_count = max(count, max_count)
        count = 1
    return max_count
