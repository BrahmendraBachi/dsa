from typing import List


def lengthOfLIS(nums: List[int]) -> int:
    dp = {}
    n = len(nums)

    def find_sequence(curr, prev=-1):
        if prev != -1 and nums[prev] >= nums[curr]:
            return 0
        if curr in dp:
            return dp[curr]
        longest_sequence = 1
        max_seq = 0
        for next_ind in range(curr + 1, n):
            local_max_seq = find_sequence(next_ind, curr)
            max_seq = max(local_max_seq, max_seq)
        dp[curr] = longest_sequence + max_seq
        return longest_sequence + max_seq

    longest = 1
    for i in range(n):
        longest = max(find_sequence(i), longest)
    return longest
