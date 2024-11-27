from typing import List


def maxArea(self, height: List[int]) -> int:
    n = len(height)
    ptr1, ptr2 = 0, n - 1
    max_area = curr_area = 0
    while ptr1 < ptr2:
        curr_area = (ptr2 - ptr1) * min(height[ptr1], height[ptr2])
        max_area = max(curr_area, max_area)

        if height[ptr1] < height[ptr2]:
            ptr1 += 1
        else:
            ptr2 -= 1
    return max_area