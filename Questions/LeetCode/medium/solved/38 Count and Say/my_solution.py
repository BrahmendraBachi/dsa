def countAndSay(n: int) -> str:
    res = "1"

    def getCountString(numStr):
        new_numStr = ""
        prev_numStr = numStr[0]
        count = 1
        for i in range(1, len(numStr)):
            if numStr[i] == prev_numStr:
                count += 1
            else:
                new_numStr = new_numStr + str(count) + str(prev_numStr)
                prev_numStr = numStr[i]
                count = 1
        return new_numStr + str(count) + str(prev_numStr)

    for i in range(2, n + 1):
        res = getCountString(res)
    return res
