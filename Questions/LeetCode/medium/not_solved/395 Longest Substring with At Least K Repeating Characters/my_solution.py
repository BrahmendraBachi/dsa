# Time Limit exceeded
from collections import defaultdict


def longestSubstring(s: str, k: int) -> int:
    dp = {}

    def find_max(substr):
        if substr in dp:
            return dp[substr]
        if len(substr) < k:
            return 0
        char_dict = defaultdict(int)
        for ch in substr:
            char_dict[ch] += 1
        if is_valid(char_dict):
            return len(substr)

        dp[substr] = max(find_max(substr[:-1]), find_max(substr[1:]))
        return dp[substr]

    def is_valid(char_dict):
        for value in char_dict.values():
            if value < k:
                return False
        return True

    return find_max(s)
