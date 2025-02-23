def mostFrequentEven(nums):
    nums_count = {}
    max_count_num = None
    max_count = 0
    for num in nums:
        if num % 2 == 0:
            if num in nums_count:
                nums_count[num] += 1
            else:
                nums_count[num] = 1
            if max_count_num is None:
                max_count = nums_count[num]
                max_count_num = num
            elif max_count == nums_count[num]:
                max_count_num = min(num, max_count_num)
            elif max_count < nums_count[num]:
                max_count_num = num
                max_count = nums_count[num]
            else:
                pass

    return -1 if max_count_num is None else max_count_num
