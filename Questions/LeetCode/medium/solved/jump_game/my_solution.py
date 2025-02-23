from typing import List


def canJump(self, nums: List[int]) -> bool:
    prev_sum = 0
    n = len(nums)
    rem = 1
    for i in range(n - 2, -1, -1):
        if rem > nums[i]:
            rem += 1
        else:
            rem = 1
    return True if rem == 1 else False


