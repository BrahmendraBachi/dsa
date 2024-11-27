def getNoOfWaysToDecode(numStr):
    if numStr[0] == "0":
        return 0

    def recursiveIteration(slate, i):
        if i >= len(numStr):
            return 1
        if len(slate) == 2:
            if 10 <= int(slate) <= 26:
                if i + 1 < len(numStr):
                    return recursiveIteration(numStr[i + 1] , i + 2)
                else:
                    return 1
            return 0
        return recursiveIteration(slate + numStr[i], i) + recursiveIteration(numStr[i], i + 1)


    return recursiveIteration(numStr[0], 1)


if __name__ == "__main__":
    print(getNoOfWaysToDecode("22626"))
