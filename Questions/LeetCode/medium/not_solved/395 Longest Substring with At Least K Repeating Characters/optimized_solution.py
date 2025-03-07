from collections import Counter


def longestSubstring(s: str, k: int) -> int:
    def get_max_substr(substr):
        if len(substr) < k:
            return 0
        dp = Counter(substr)
        lesser_count_chars = []
        for item, value in dp.items():
            if value < k:
                lesser_count_chars.append(item)
        if len(lesser_count_chars) == 0:
            return len(substr)

        ind = 0
        for ind in range(len(substr)):
            if substr[ind] in lesser_count_chars:
                break
        return max(get_max_substr(substr[:ind]), get_max_substr(substr[ind + 1:]))

    return get_max_substr(s)