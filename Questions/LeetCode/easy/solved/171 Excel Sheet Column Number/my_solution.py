def titleToNumber(self, columnTitle: str) -> int:
    _pow = 0
    id = 0
    for i in range(len(columnTitle) - 1, -1, -1):
        id += (ord(columnTitle[i]) - ord('A') + 1) * (26 ** _pow)
        _pow += 1
    return id