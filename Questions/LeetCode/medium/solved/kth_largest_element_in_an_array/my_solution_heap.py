from heapq import heapify, heappop


def findKthLargest(nums, k):
    heapify(nums)
    n = len(nums)
    for i in range(n - k):
        heappop(nums)
    return nums[0]
