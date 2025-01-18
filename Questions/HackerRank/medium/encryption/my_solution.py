import math
import os


def encryption(s):
    # Write your code here
    s = list(s.replace(" ", ""))
    strLen = len(s)
    sqRoot = len(s) ** 0.5
    enc_list = []
    s = list(s)

    row = math.floor(sqRoot)
    col = math.ceil(sqRoot)

    if row * col <= strLen:
        row += 1

    for i in range(row):
        if (i * col) + col >= strLen:
            enc_list.append(s[(i * col):])
            continue
        enc_list.append(s[(i * col):((i * col) + col)])

    final_str = ''
    for i in range(col):
        res = ''
        for enc_str in enc_list:
            if i < len(enc_str):
                res = res + enc_str[i]
        final_str += res + " "

    return final_str


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    inp_s = input()
    result = encryption(inp_s)
    fptr.write(result + '\n')
    fptr.close()
