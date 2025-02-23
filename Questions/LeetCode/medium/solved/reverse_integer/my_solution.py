def reverse(x):
    isNegative = False
    x = list(str(x))
    if x[0] == "-":
        isNegative = True
        del x[0]
    x = "".join(x[::-1])
    if isNegative:
        x = "-" + x
    x = int(x)

    return 0 if x > (2 ** 31 - 1) or x < (-1 * 2 ** 31) else x
