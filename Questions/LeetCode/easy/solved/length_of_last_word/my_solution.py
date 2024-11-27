def lengthOfLastWord(self, s: str) -> int:
    start = False
    count = 0
    for i in range(len(s) - 1, -1, -1):
        if s[i] == " " and not start:
            continue
        if s[i] == " " and start:
            break
        if not start:
            start = True
        count += 1
    return count