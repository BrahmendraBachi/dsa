def strStr(self, haystack: str, needle: str) -> int:
    i = j = 0
    n = len(haystack)
    m = len(needle)
    if n < m or n == 0 or m == 0:
        return -1
    rem = 0
    while i + j < n:
        if haystack[i + j] == needle[j]:
            if j + 1 == m:
                return i
            j += 1
            continue
        i += 1
        j = 0
    return -1