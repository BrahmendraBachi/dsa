def numDecodings(s: str) -> int:
    last2 = 0
    last1 = 1
    for i in range(len(s) - 1, -1, -1):
        temp = last1

        if i + 1 < len(s) and int(s[i: i + 2]) <= 26:
            temp += last2

        if s[i] == '0':
            temp = 0

        last2 = last1
        last1 = temp
    return last1
