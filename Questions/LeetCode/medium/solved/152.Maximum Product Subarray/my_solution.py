from typing import List


def maxProduct(nums: List[int]) -> int:
    def find_max(curr_max_prod):
        total_curr_prod = 1
        curr_prod = 1

        for num in nums[::-1]:
            curr_prod *= num
            total_curr_prod *= num

            curr_max_prod = max(curr_prod, total_curr_prod, curr_max_prod)

            if curr_prod <= 0:
                curr_prod = 1
            if total_curr_prod == 0:
                total_curr_prod = 1
        return curr_max_prod

    max_prod = float('-inf')
    max_prod = find_max(max_prod)
    nums = nums[::-1]
    max_prod = find_max(max_prod)
    return max_prod
