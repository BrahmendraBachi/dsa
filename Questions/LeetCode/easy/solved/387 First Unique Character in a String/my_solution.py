from collections import Counter


def firstUniqChar(s: str) -> int:
    counter = Counter(s)
    for i, ch in enumerate(s):
        if counter[ch] == 1:
            return i
    return -1