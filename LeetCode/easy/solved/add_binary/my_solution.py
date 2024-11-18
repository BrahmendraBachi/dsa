def addBinary(self, a: str, b: str) -> str:
    len_a, len_b = len(a), len(b)
    if len(a) < len(b):
        a = "0" * (len(b) - len(a)) + a
    else:
        b = "0" * (len(a) - len(b)) + b
    n = len(a) - 1
    res = ""
    carr = 0
    while n >= 0:
        bit1, bit2 = int(a[n]), int(b[n])
        bit_sum = bit1 + bit2 + carr
        if bit_sum == 3:
            res = "1" + res
            carr = 1
        elif bit_sum == 2:
            res = "0" + res
            carr = 1
        else:
            res = str(bit_sum) + res
            carr = 0
        n -= 1
    if carr:
        res = str(carr) + res
    return res
