def countKeyChanges(self, s: str) -> int:
    prev = s[0]
    n = len(s)
    count = 0
    for i in range(1, n):
        if prev.lower() != s[i].lower():
            count += 1
        prev = s[i]
    return count