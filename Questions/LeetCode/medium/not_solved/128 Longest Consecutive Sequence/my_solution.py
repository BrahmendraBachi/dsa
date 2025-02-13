def longestConsecutive(nums):
    if len(nums) == 0:
        return 0
    nums = set(nums)
    count_hash = {}
    count = max_count = 0
    for num in nums:
        count += 1
        temp = num
        while (num - 1) in nums:
            if num - 1 in count_hash:
                count += count_hash[num - 1]
                break
            count += 1
            num -= 1
        count_hash[temp] = count
        max_count = max(count, max_count)
        count = 0

    return max_count
