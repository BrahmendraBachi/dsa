def removeDuplicates(self, nums: List[int]) -> int:
    n = len(nums)
    isAlreadyFound = False
    curr_num = nums[0]
    for i in range(1, n):
        if nums[i] == curr_num:
            if isAlreadyFound:
                nums[i] = None
            else:
                isAlreadyFound = True
            continue
        curr_num = nums[i]
        isAlreadyFound = False
    shift = 0
    for i in range(n):
        if nums[i] == None:
            shift += 1
            continue
        nums[i - shift], nums[i] = nums[i], nums[i - shift]
    return n - shift