def twoSum_1(numbers, target):
    left, right = 0, len(numbers) - 1
    while left < right:
        total = numbers[left] + numbers[right]
        if total == target:
            return [left + 1, right + 1]
        elif total > target:
            right -= 1
        else:
            left += 1
    return []
