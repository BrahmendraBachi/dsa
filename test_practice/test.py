def jump(nums):
    curr_step = 0

    def canJump(curr_index):
        if curr_index == len(nums) - 1:
            return True
        maxJump = nums[curr_index]
        if maxJump == 0:
            return False
        start = curr_index + 1
        for curr_index in range(start, curr_index + nums[curr_index] + 1):
            return canJump(curr_index)
        return False

    dp = [None] * len(nums)

    def minStepsToJump(curr_index):
        if dp[curr_index] is not None:
            return dp[curr_index]
        if curr_index >= len(nums) - 1:
            return 1
        maxJump = nums[curr_index]
        if maxJump == 0:
            return 0
        start = curr_index + 1
        end = curr_index + nums[curr_index] + 1
        for i in range(start, end):
            count = minStepsToJump(i)
            dp[curr_index] = count if dp[curr_index] is None else min(count, dp[curr_index])
        return dp[curr_index]

    return minStepsToJump(curr_step)


if __name__ == '__main__':
    arr1 = [2, 3, 1, 1, 4]
    arr2 = [3, 2, 1, 0, 4]
    print(jump(arr1))
