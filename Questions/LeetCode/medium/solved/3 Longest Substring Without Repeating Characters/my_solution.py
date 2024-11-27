def lengthOfLongestSubstring(s: str) -> int:
    n = len(s)
    if n == 1 or n == 0:
        return n
    start, end, max_count = 0, 1, 0
    str_dict = {s[start]: 1}
    while end < n:
        if start == end:
            end = start + 1
            continue
        if s[end] in str_dict:
            del str_dict[s[start]]
            max_count = max(max_count, end - start)
            start += 1
            str_dict[s[start]] = 1
        else:
            str_dict[s[end]] = 1
            end += 1
    max_count = max(max_count, end - start)

    return max_count
