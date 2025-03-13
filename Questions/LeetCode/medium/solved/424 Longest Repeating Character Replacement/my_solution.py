from collections import defaultdict


def characterReplacement(self, s: str, k: int) -> int:
    curr_count = defaultdict(int)
    max_count = 0
    i = j = 0
    n = len(s)
    curr_count[s[j]] += 1
    while j < n:
        curr_len = (j - i) + 1
        curr_max = max(curr_count.values())
        if curr_len - curr_max <= k:
            max_count = max(curr_len, max_count)
            if j + 1 >= n:
                break
            j += 1
            curr_count[s[j]] += 1
        else:
            curr_count[s[i]] -= 1
            i += 1
    return max_count