from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sequence_array = [nums[0]]
        n = len(nums)
        for i in range(1, n):
            if sequence_array[-1] >= nums[i]:
                ind = self.find_index(sequence_array, nums[i], 0, len(sequence_array) - 1)
                print(sequence_array, ind, nums[i])
                sequence_array[ind] = nums[i]
            else:
                sequence_array.append(nums[i])
        return len(sequence_array)

    def find_index(self, arr, val, l, r):
        if l > r:
            return l
        m = (l + r) // 2
        if arr[m] == val:
            return m
        elif arr[m] <= val:
            return self.find_index(arr, val, m + 1, r)
        else:
            return self.find_index(arr, val, l, m - 1)
