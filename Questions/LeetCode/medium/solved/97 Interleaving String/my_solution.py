def isInterleave(s1: str, s2: str, s3: str) -> bool:
    if len(s1) + len(s2) != len(s3):
        return False

    dp = {}

    def isValid(ind1, ind2):
        if (ind1, ind2) in dp:
            return dp[(ind1, ind2)]
        if ind1 + ind2 == len(s3):
            return True
        isValid1 = isValid2 = False
        if ind1 < len(s1) and s1[ind1] == s3[ind1 + ind2]:
            isValid1 = isValid(ind1 + 1, ind2)
        if ind2 < len(s2) and s2[ind2] == s3[ind1 + ind2]:
            isValid2 = isValid(ind1, ind2 + 1)

        dp[ind1, ind2] = isValid1 or isValid2

        return dp[ind1, ind2]

    return isValid(0, 0)
