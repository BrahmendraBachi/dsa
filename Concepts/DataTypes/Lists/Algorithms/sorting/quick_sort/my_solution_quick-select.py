from typing import List


def findKthLargest(self, nums: List[int], k: int) -> int:
    target = len(nums) - k

    def quickSelect(low=0, high=None):
        if high is None:
            high = len(nums) - 1
        if low >= high:
            return nums[low]
        pivot = self.partition(nums, low, high)
        if pivot == target:
            return nums[pivot]
        elif pivot > target:
            return quickSelect(low, pivot - 1)
        else:
            return quickSelect(pivot + 1, high)

    return quickSelect()


def partition(self, arr, low, high):
    pivot_index = random.randint(low, high)  # Random pivot selection
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]  # Swap pivot to end
    pivot = arr[high]
    j = low - 1

    for i in range(low, high):
        if arr[i] < arr[high]:
            j += 1
            arr[j], arr[i] = arr[i], arr[j]
    j += 1
    arr[j], arr[high] = arr[high], arr[j]
    return j