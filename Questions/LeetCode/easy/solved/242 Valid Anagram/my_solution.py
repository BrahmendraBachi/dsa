from collections import Counter


def isAnagram(s: str, t: str) -> bool:
    counter_s = Counter(s)
    counter_t = Counter(t)
    for item, value in counter_s.items():
        if counter_t[item] != value:
            return False
    for item, value in counter_t.items():
        if counter_s[item] != value:
            return False

    return True