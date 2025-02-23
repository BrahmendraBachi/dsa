def topKFrequent(nums, k):
    nums_count = {}
    for num in nums:
        if num in nums_count:
            nums_count[num] += 1
        else:
            nums_count[num] = 1

    count_nums = {i: [] for i in range(1, len(nums) + 1)}
    for num, count in nums_count.items():
        count_nums[count].append(num)

    elements = []
    for count in range(len(nums), 0, -1):
        if len(count_nums[count]) == 0:
            continue
        for ele in count_nums[count]:
            elements.append(ele)
            if len(elements) == k:
                return elements
    return elements
