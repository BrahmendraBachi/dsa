import math
import os
import random
import re
import sys


def plusMinus(arr):
    pos, neg, zer = 0, 0, 0
    n = len(arr)
    for i in arr:
        if i > 0:
            pos += 1
        elif i < 0:
            neg += 1
        else:
            zer += 1
    print(round((pos / n), 6))
    print(round((neg / n), 6))
    print(round((zer / n), 6))


if __name__ == '__main__':
    len_n = int(input().strip())
    input_1 = list(map(int, input().rstrip().split()))
    plusMinus(input_1)
