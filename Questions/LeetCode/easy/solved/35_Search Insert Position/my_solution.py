def searchInsert(nums, target):
    def binary_search(left, right):
        if left > right:
            return left
        m = (left + right) // 2
        if target == nums[m]:
            return m
        return binary_search(m + 1, right) if target > nums[m] else binary_search(left, m - 1)
    return binary_search(0, len(nums) - 1)
