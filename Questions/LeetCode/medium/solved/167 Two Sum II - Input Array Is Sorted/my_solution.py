from typing import List


def twoSum(numbers: List[int], target: int) -> List[int]:
    ptr1, ptr2 = 0, len(numbers) - 1
    while ptr1 < ptr2:
        s = numbers[ptr1] + numbers[ptr2]
        if s < target:
            ptr1 += 1
        if s > target:
            ptr2 -= 1
        if s == target:
            return [ptr1 + 1, ptr2 + 1]
