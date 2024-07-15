def minRequiredJumps(arr):
    result = {}

    def recursiveMethod(nums, curr_step=0, count=0):
        if curr_step in result:
            return count + result[curr_step]
        if curr_step >= len(nums) - 1:
            return count
        if nums[curr_step] == 0:
            return 0
        start = curr_step + 1
        end = start + nums[curr_step]
        for step in range(start, end):
            count = 0
            count = recursiveMethod(nums, step, count + 1)
            if count == 0:
                continue
            result[curr_step] = min(count, result[curr_step]) if (curr_step in result and count != 0) else count
        return 1 + result[curr_step] if count != 0 else 0

    recursiveMethod(arr)
    print(result)
    return result[0]


if __name__ == '__main__':
    input_1 = [2, 3, 1, 1, 4]
    input_2 = [2, 3, 0, 1, 4]
    input_3 = [4, 2, 1, 0, 4]
    input_4 = [5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]
    print(minRequiredJumps(input_4))
