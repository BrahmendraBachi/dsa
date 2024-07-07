def isValid(self, s: str) -> bool:
    s = list(s)
    res = []
    for brace in s:
        if brace == "}":
            if len(res) and res[-1] == "{":
                res.pop()
            else:
                return False
        elif brace == ")":
            if len(res) and res[-1] == "(":
                res.pop()
            else:
                return False
        elif brace == "]":
            if len(res) and res[-1] == "[":
                res.pop()
            else:
                return False
        else:
            res.append(brace)
    return len(res) == 0
