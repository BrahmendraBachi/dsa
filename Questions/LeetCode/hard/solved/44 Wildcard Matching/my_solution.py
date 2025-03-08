def isMatch(s: str, p: str) -> bool:
    visited = set()

    def is_valid(ind1, ind2):
        isCurrValid = False
        if (ind1, ind2) in visited:
            return False

        if ind1 == len(s) and ind2 == len(p):
            return True

        elif ind1 == len(s):
            return all(ch == '*' for ch in p[ind2:])

        elif ind2 >= len(p):
            return False

        elif p[ind2] == "*":
            isCurrValid = isCurrValid or is_valid(ind1 + 1, ind2) or is_valid(ind1, ind2 + 1)

        elif p[ind2] == "?" or s[ind1] == p[ind2]:
            isCurrValid = isCurrValid or is_valid(ind1 + 1, ind2 + 1)

        else:
            return False

        visited.add((ind1, ind2))

        return isCurrValid

    return is_valid(0, 0)
