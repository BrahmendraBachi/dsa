from typing import List


def trap(height: List[int]) -> int:
    n = len(height)
    curr_max_ind = 0

    for i in range(1, n):
        if height[i] >= height[curr_max_ind]:
            curr_max_ind = i

    total_trap = 0
    ptr1, ptr2 = 0, 1
    curr_sum = 0
    while ptr2 <= curr_max_ind:
        if height[ptr2] >= height[ptr1]:
            total_trap += (min(height[ptr2], height[ptr1]) * (ptr2 - ptr1 - 1)) - curr_sum
            curr_sum = 0
            ptr1 = ptr2
        else:
            curr_sum += height[ptr2]
        ptr2 += 1

    ptr1, ptr2 = n - 1, n - 2
    curr_sum = 0
    while curr_max_ind <= ptr2:
        if height[ptr2] >= height[ptr1]:
            total_trap += (min(height[ptr2], height[ptr1]) * (ptr1 - ptr2 - 1) - curr_sum)
            ptr1 = ptr2
            curr_sum = 0
        else:
            curr_sum += height[ptr2]
        ptr2 -= 1

    return total_trap
